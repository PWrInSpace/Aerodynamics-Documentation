import matplotlib.pyplot as plt

def plotData():
    values1 = [0.459034328105048, 0.404336651338853, 0.396962392205453, 0.397011926120074, 0.399242315686303, 0.40139809734908, 0.406074799502895, 0.411070061311167, 0.4193379544368, 0.418919542823116]
    values2 = [0.633124100074822, 0.553129250912094, 0.529854748184211, 0.518196961417704, 0.514490981639282, 0.512583409743801, 0.512793324549311, 0.516679370180853, 0.525676775960665, 0.524400388412621]
    values1.reverse()
    values2.reverse()
    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    plt.plot(x, values1, label='R6 Endcone', color='r', marker='o', linewidth=2, markersize=8)
    plt.plot(x, values2, label='R6 NoEndcone', color=(0.4, 0.4, 0.4), marker='s', linewidth=2, markersize=8)
    plt.xlabel('Mach')
    plt.ylabel('Drag Coefficient')
    plt.title('Drag Coefficient vs Mach')
    plt.legend()
    plt.grid(True)
    plt.show()

plotData()