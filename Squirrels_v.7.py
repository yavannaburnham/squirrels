import numpy as np
import matplotlib.pyplot as plt


#Set default parameters:
GainPeanut = 5
GainHazel = 9
TrialNo = np.linspace(1, 10, num=10)

SearchTimePeanut = np.linspace(1, 1, num=10)
SearchTimeHazel = np.linspace(1, 10, num=10)

HandleTimePeanut = 2
HandleTimeHazel = 1

SearchEnergyPeanut = np.linspace(1, 1, num=10)
SearchEnergyHazel = np.linspace(1, 10, num=10)

HandleEnergyPeanut = 2
HandleEnergyHazel = 1

#Set default currencies:
NetRatePeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchTimePeanut + HandleTimePeanut)
GrossPeanut = (GainPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
EfficPeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)

NetRateHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchTimeHazel + HandleTimeHazel)
GrossHazel = (GainHazel) / (SearchEnergyHazel + HandleEnergyHazel)
EfficHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchEnergyHazel + HandleEnergyHazel)

#Define plot as a function
def plot():
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    fig.suptitle('Currency Comparison')

    ax1.plot(NetRateHazel, label='Hazelnut')
    ax1.plot(NetRatePeanut, label='Peanut')
    ax1.legend()
    ax1.set_xlabel('Trial number')
    ax1.set_ylabel('Net rate')
    ax1.set_yticks([0, 1, 2, 3, 4, 5])
    ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], TrialNo)

    ax2.plot(GrossHazel, label='Hazelnut')
    ax2.plot(GrossPeanut, label='Peanut')
    ax2.legend()
    ax2.set_xlabel('Trial number')
    ax2.set_ylabel('Gross efficiency')
    ax2.set_yticks([0, 1, 2, 3, 4, 5])
    ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], TrialNo)

    ax3.plot(EfficHazel, label='Hazelnut')
    ax3.plot(EfficPeanut, label='Peanut')
    ax3.legend()
    ax3.set_xlabel('Trial number')
    ax3.set_ylabel('Net efficiency')
    ax3.set_yticks([0, 1, 2, 3, 4, 5])
    ax3.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], TrialNo)
    plt.show()
def currencies(Gain,SearchEnergy,HandleEnergy,SearchTime,HandleTime):
    NetRate = (Gain - SearchEnergy - HandleEnergy) / (SearchTime + HandleTime)
    Gross = (Gain) / (SearchEnergy + HandleEnergy)
    Effic = (Gain - SearchEnergy - HandleEnergy) / (SearchEnergy + HandleEnergy)
    return [NetRate, Gross, Effic]

currencies_output=currencies(GainPeanut,SearchEnergyPeanut,HandleEnergyPeanut,SearchTimePeanut,HandleTimePeanut)
NetRatePeanut=currencies_output[1]
GrossPeanut=currencies_output[2]
EfficPeanut=currencies_output[3]


for varloop in range(Nvarloops):
    GainPeanut = (varloop/Nvarloops)*(maxval-minval)+minval


userChoice = input(
    "\n  Input the number of the variable you wish to change:"
    " \n (1. Energy gain) \n (2. Search time) \n (3. Handling time) \n (4. Energy used searching) \n"
    " (5. Energy used handling) \n")

if userChoice == "1":
    userStart = input("\n Input the number of the nut you wish to change"
                      " the energy gain of: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        GainPeanut = int(input("How many Kcals does the squirrel gain from eating a peanut?: "))


        GainPeanut = np.linspace(minval, maxval, num=10)


        NetRatePeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchTimePeanut + HandleTimePeanut)
        GrossPeanut = (GainPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        EfficPeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        plot()

    print()
    if userStart == "2":
        GainHazel = int(input("How many Kcals does the squirrel gain from eating a hazelnut?: "))

        NetRateHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchTimeHazel + HandleTimeHazel)
        GrossHazel = (GainHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        EfficHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        plot()

if userChoice == "2":
    userStart = input("\n Input the number of the nut you wish to change"
                        " the search time of: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        UserPeanut = int(input("How many seconds does it take the squirrel to find the peanut?: "))
        SearchTimePeanut = np.linspace(UserPeanut, UserPeanut, num=10)

        NetRatePeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchTimePeanut + HandleTimePeanut)
        GrossPeanut = (GainPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        EfficPeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        plot()

    if userStart == "2":
        UserHazel = int(input("How many seconds does it take the squirrel to find the hazelnut? "
                              "(Search time will continue to increase by "
                          "the value you input for each subsequent trial): "))
        SearchTimeHazelHazel = np.linspace(UserHazel, (UserHazel*10), num=10)
        NetRateHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchTimeHazel + HandleTimeHazel)
        GrossHazel = (GainHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        EfficHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        plot()


if userChoice == "3":
    userStart = input("\n Input the number of the nut you wish to change"
                              " the handling time for: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        HandleTimePeanut = int(input("How many seconds does it take the squirrel to handle the peanut?: "))
        NetRatePeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchTimePeanut + HandleTimePeanut)
        GrossPeanut = (GainPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        EfficPeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        plot()

    print()
    if userStart == "2":
        HandleTimeHazel = int(input("How many seconds does it take the squirrel to handle the hazelnut?: "))
        NetRateHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchTimeHazel + HandleTimeHazel)
        GrossHazel = (GainHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        EfficHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        plot()

if userChoice == "4":
    userStart = input("\n Input the number of the nut you wish to change"
                              " the energy used searching for: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        UserPeanut = int(input("How many Kcals does the squirrel use to find the peanut?: "))
        SearchEnergyPeanut = np.linspace((UserPeanut), (UserPeanut), num=10)
        NetRatePeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchTimePeanut + HandleTimePeanut)
        GrossPeanut = (GainPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        EfficPeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        plot()

    print()
    if userStart == "2":
        UserHazel = int(input("How many Kcals does the squirrel use to find the hazelnut?: "))
        SearchEnergyHazel = np.linspace((UserHazel), (UserHazel * 10), num=10)
        NetRateHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchTimeHazel + HandleTimeHazel)
        GrossHazel = (GainHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        EfficHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        plot()


if userChoice == "5":
    userStart = input("\n Input the number of the nut you wish to change"
                              " the energy used handling for: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        UserPeanut = int(input("How many Kcals does the squirrel use to handle the peanut?: "))
        HandleEnergyPeanut = np.linspace((UserPeanut), (UserPeanut), num=10)
        NetRatePeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchTimePeanut + HandleTimePeanut)
        GrossPeanut = (GainPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        EfficPeanut = (GainPeanut - SearchEnergyPeanut - HandleEnergyPeanut) / (SearchEnergyPeanut + HandleEnergyPeanut)
        plot()

    if userStart == "2":
        UserHazel = int(input("How many Kcals does the squirrel use to handle the hazelnut?: "))
        HandleEnergyHazel = np.linspace((UserHazel), (UserHazel), num=10)
        NetRateHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchTimeHazel + HandleTimeHazel)
        GrossHazel = (GainHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        EfficHazel = (GainHazel - SearchEnergyHazel - HandleEnergyHazel) / (SearchEnergyHazel + HandleEnergyHazel)
        plot()


