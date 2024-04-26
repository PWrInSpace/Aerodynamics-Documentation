import math

def getAverage10():
    values1 = [0.459034328105048, 0.404336651338853, 0.396962392205453, 0.397011926120074, 0.399242315686303, 0.40139809734908, 0.406074799502895, 0.411070061311167, 0.4193379544368, 0.418919542823116]
    average1 = sum(values1) / len(values1)
    print("Average of R6 Endcone 10: ", average1)

    values2 = [0.633124100074822, 0.553129250912094, 0.529854748184211, 0.518196961417704, 0.514490981639282, 0.512583409743801, 0.512793324549311, 0.516679370180853, 0.525676775960665, 0.524400388412621]
    average2 = sum(values2) / len(values2)
    print("Average of R6 No Endcone 10: ", average2)

    print("Difference of average values 10: ", average2 - average1)

    print("Procentage ", (average2 - average1) / average1 * 100)

def getAverage06():
    values1 = [0.399242315686303, 0.40139809734908, 0.406074799502895, 0.411070061311167, 0.4193379544368, 0.418919542823116]
    average1 = sum(values1) / len(values1)
    print("Average of R6 Endcone 60: ", average1)

    values2 = [0.514490981639282, 0.512583409743801, 0.512793324549311, 0.516679370180853, 0.525676775960665, 0.524400388412621]
    average2 = sum(values2) / len(values2)
    print("Average of R6 No Endcone 60: ", average2)

    print("Difference of average values 60: ", average2 - average1)

    print("Procentage ", (average2 - average1) / average1 * 100)

getAverage10()
print()
getAverage06()
