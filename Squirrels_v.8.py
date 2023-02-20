import numpy as np
import matplotlib.pyplot as plt

#Set default values:
GainPeanut = 5
GainHazel = 9
TrialNo = np.linspace(1, 10, num=10)

SearchTimePeanut = np.linspace(1, 1, num=10)
SearchTimeHazel = np.linspace(5, 5, num=10)

HandleTimePeanut = 2
HandleTimeHazel = 1

SearchEnergyPeanut = np.linspace(1, 1, num=10)
SearchEnergyHazel = np.linspace(5, 5, num=10)

HandleEnergyPeanut = 2
HandleEnergyHazel = 1

#Set currencies as a function:
def currencies(Gain, SearchEnergy, HandleEnergy, SearchTime, HandleTime):
    NetRate = (Gain - SearchEnergy - HandleEnergy) / (SearchTime + HandleTime)
    NetEfficiency = (Gain - SearchEnergy - HandleEnergy) / (SearchEnergy + HandleEnergy)
    GrossRate = (Gain / (SearchTime + HandleTime))
    GrossEfficiency = (Gain / (SearchEnergy + HandleEnergy))
    return [NetRate, NetEfficiency, GrossRate, GrossEfficiency]

currencies_output = currencies(GainPeanut, SearchEnergyPeanut, HandleEnergyPeanut, SearchTimePeanut, HandleTimePeanut)
NetRatePeanut = currencies_output[1]
NetEfficiencyPeanut = currencies_output[2]
GrossRatePeanut = currencies_output[3]

currencies_output = currencies(GainHazel, SearchEnergyHazel, HandleEnergyHazel, SearchTimeHazel, HandleTimeHazel)
NetRateHazel = currencies_output[1]
NetEfficiencyHazel = currencies_output[2]
GrossRateHazel = currencies_output[3]


#Generate plot as a function:
def plot():
    fig, (ax1) = plt.subplots(1, 1)
    fig.suptitle('Currency Comparison')

    ax1.plot(NetRateHazel, label='Hazelnut')
    ax1.plot(NetRatePeanut, label='Peanut')
    ax1.legend()
    ax1.set_xlabel('Kcal gained from peanut')
    ax1.set_ylabel('Net rate')
    ax1.set_yticks([0, 1, 2, 3, 4, 5])
    ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], TrialNo)

    plt.show()

userChoice = input(
    "\n  Input the number of the variable you wish to change:"
    " \n (1. Energy gain)")

if userChoice == "1":
    userStart = input("\n Input the number of the nut you wish to change"
                      ": \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        minval, maxval = (input("Enter a minimum and maximum value: ").split())
        print("Kcal gained ranges between {} and {}".format(minval, maxval))
        print()
        minval_flt = float(minval)
        maxval_flt = float(maxval)
        GainPeanut = np.linspace(minval_flt, maxval_flt, num=10)


    if userStart == "2":
        minval, maxval = (input("Enter two values: ").split())
        print("Kcal gained ranges between {} and {}".format(minval, maxval))
        print()
        minval_flt = float(minval)
        maxval_flt = float(maxval)
        GainHazel = np.linspace(minval_flt, maxval_flt, num=10)

    NetRatePeanut
    plot()









