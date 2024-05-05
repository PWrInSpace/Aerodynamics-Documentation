import matplotlib.pyplot as plt

def plotEndcone():
    x = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]
    y = [1.74, 1.76, 1.77, 1.78, 1.78, 1.79, 1.79, 1.79, 1.8, 1.8, 1.8]
    plt.plot(x, y, 'o-')
    plt.xlabel("Angle of Endcone [degrees]")
    plt.ylabel("Stability[cal]")
    plt.title('Stability vs Angle of Endcone')
    plt.grid(True)
    plt.show()

plotEndcone()

def plotSweep():
    x = [23, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
    y = [1.07, 1.37, 1.51, 1.61, 1.68, 1.73, 1.75, 1.77, 1.77, 1.77, 1.76, 1.75, 1.73]
    plt.plot(x, y, 'o-')
    plt.xlabel("Sweep angle [degrees]")
    plt.ylabel("Stability[cal]")
    plt.title('Stability vs Sweep angle')
    plt.grid(True)
    plt.show()

plotSweep()