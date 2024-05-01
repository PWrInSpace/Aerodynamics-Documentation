import matplotlib.pyplot as plt
from CSVReader import CSVReader

# Create an instance of the CSVReader class
reader = CSVReader()

# Call the desired function from the CSVReader class
content = reader.readCSV('export.csv')

# Calculate average values for each row
averages = []
key, count = int(0), int(0)
averages.append([key, 0])

for i in range(0, len(content)):
    if(key == int(content[i][1])):
        count += 1
    else:
        averages[key][1] /= count
        key += 1
        count = 1
        averages.append([key, 0])  # Append a new sublist for the new key

    averages[key][1] += float(content[i][2])

averages[15][1] /=6

def plotAverages(averages):
    # Separate keys and average values into two lists for plotting
    keys = [item[0] for item in averages]
    values = [item[1] for item in averages]

    # Plot averages
    plt.plot(keys, values, 'o-')
    plt.xlabel("Angle of Endcone")
    plt.ylabel("Average Force value")
    plt.title('Average values of Force vs Angle of endcone')
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
    x2 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(29, 23, -1)]
    x3 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(53, 47, -1)]

    # Plot values
    plt.figure()  # Create a new figure
    plt.plot(y, x1, 'o-', label='Angle of 0 degrees')
    plt.plot(y, x2, 'o-', label='Angle of 4 degrees')
    plt.plot(y, x3, 'o-', label='Angle of 8 degrees')
    plt.xlabel("Mach")
    plt.ylabel("Drag coefficient")
    plt.title('Cd Values for Different Angles of Endcone')
    plt.legend()  # Add a legend
    plt.show()

def plotCdVsAngle(content):
    # Extract values from content
    y = [item[0] for item in averages]
    x1 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(4, 95, 6)]
    x2 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(2, 93, 6)]
    x3 = [ForceToCD(float(content[i][2]), float(content[i][0])) for i in range(0, 91, 6)]

    # Plot values
    plt.figure()  # Create a new figure
    plt.plot(y, x1, 'o-', label='Mach 0.2')
    plt.plot(y, x2, 'o-', label='Mach 0.4')
    plt.plot(y, x3, 'o-', label='Mach 0.6')
    plt.xlabel("Angle of Endcone")
    plt.ylabel("Drag coefficient")
    plt.title('Cd Value vs Angle of Endcone')
    plt.legend()  # Add a legend
    plt.show()

plotAverages(averages)

plotExampleValues(content)

plotCdVsAngle(content)






