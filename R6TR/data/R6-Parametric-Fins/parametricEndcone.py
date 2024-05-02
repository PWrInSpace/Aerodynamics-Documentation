import matplotlib.pyplot as plt
from CSVReader import CSVReader
import numpy as np
import seaborn as sns
import pandas as pd

# Create an instance of the CSVReader class
reader = CSVReader()

# Call the desired function from the CSVReader class
content = reader.readCSV('export.csv')

# Initialize a dictionary to store the sum and count for each unique key
sums = {}
counts = {}

for i in range(len(content)):
    key = int(content[i][1])
    value = float(content[i][2])

    # If the key is not in the dictionaries, add it with the current value and a count of 1
    if key not in sums:
        sums[key] = value
        counts[key] = 1
    # If the key is already in the dictionaries, add the current value to the sum and increment the count
    else:
        sums[key] += value
        counts[key] += 1

# Calculate the average for each key and store it in the averages list
averages = [[key, sums[key] / counts[key]] for key in sums]

def plotAverages(averages):
    # Separate keys and average values into two lists for plotting
    keys = [item[0] for item in averages]
    values = [item[1] for item in averages]
    

    # Plot averages
    plt.plot(keys, values, 'o-')
    plt.xlabel("Sweep Angle")
    plt.ylabel("Average Force value")
    plt.title('Average values of Force vs Sweep Angle')
    plt.show()




def ForceToCD(force, velocity):
    # Constants for ForceToCD function
    REF_AREA = 0.018384843
    DENSITY = 1.225
    return 2 * force / (DENSITY * velocity**2 * REF_AREA)

def plotExampleValues(content):
    # Extract values from content
    y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    x1 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(5, -1, -1)]
    x2 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(41, 35, -1)]
    x3 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(77, 71, -1)]

    # Plot values
    plt.figure()  # Create a new figure
    plt.plot(y, x1, 'o-', label='Angle of 30 degrees')
    plt.plot(y, x2, 'o-', label='Angle of 60 degrees')
    plt.plot(y, x3, 'o-', label='Angle of 90 degrees')
    plt.xlabel("Mach")
    plt.ylabel("Drag coefficient")
    plt.title('Cd Values for Different Sweep Angles')
    plt.legend()  # Add a legend
    plt.show()

def plotCdVsAngle(content):
    # Extract values from content
    y = [item[0] for item in averages]
    
    x1 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(4, 78, 6)]
    x2 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(2, 76, 6)]
    x3 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(0, 74, 6)]

    # Plot values
    plt.figure()  # Create a new figure
    plt.plot(y, x1, 'o-', label='Mach 0.2')
    plt.plot(y, x2, 'o-', label='Mach 0.4')
    plt.plot(y, x3, 'o-', label='Mach 0.6')
    plt.xlabel("Sweep Angle")
    plt.ylabel("Drag coefficient")
    plt.title('Cd Value vs Sweep Angle')
    plt.legend()  # Add a legend
    plt.show()

plotAverages(averages)

plotExampleValues(content)

plotCdVsAngle(content)

def plotCdVsAngleV2(content, mach_values):
    # Initialize a 2D array for the drag coefficients
    cd_values = np.zeros((len(averages), len(mach_values)))

    # Calculate the drag coefficient for each Mach number and angle
    for i in range(len(averages)):
        for j in range(len(mach_values)):
            cd_values[i][j] = ForceToCD(float(content[i*6 + j][2]), float(content[i*6 + j][0]))

    # Convert the 2D array to a DataFrame
    df = pd.DataFrame(cd_values, index=[item[0] for item in averages], columns=mach_values)

    # Plot the heatmap
    plt.figure(figsize=(10, 8))  # Create a new figure
    sns.heatmap(df, cmap='hot', annot=True, fmt=".2f")
    plt.xlabel("Mach")
    plt.ylabel("Sweep Angle")
    plt.title('Cd Value vs Sweep Angle and Mach')
    plt.show()

# Call the function with the Mach values as a parameter
plotCdVsAngleV2(content, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])






