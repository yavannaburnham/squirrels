import numpy as np
import matplotlib.pyplot as plt

#Set default parameters
gainPeanut = 5
gainHazel = 9

searchPeanut = np.linspace(1, 1, num=10)
searchHazel = np.linspace(1, 10, num=10)
trialNo = np.linspace(1, 10, num=10) #Set no. of trials

handlePeanut = 2
handleHazel = 1

usedPeanut = searchPeanut + handlePeanut
netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
grossPeanut = (gainPeanut / usedPeanut)
efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)

usedHazel = searchHazel + handleHazel
netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)
grossHazel = (gainHazel / usedHazel)
efficHazel = (gainHazel - usedHazel) / (usedHazel)

#Define plot as a function
def plot():
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    fig.suptitle('Currency Comparison')

    ax1.plot(netrateHazel, label='Hazelnut')
    ax1.plot(netratePeanut, label='Peanut')
    ax1.legend()
    ax1.set_xlabel('Trial number')
    ax1.set_ylabel('Net rate')
    ax1.set_yticks([0, 1, 2, 3, 4, 5])
    ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], trialNo)

    ax2.plot(grossHazel, label='Hazelnut')
    ax2.plot(grossPeanut, label='Peanut')
    ax2.legend()
    ax2.set_xlabel('Trial number')
    ax2.set_ylabel('Gross efficiency')
    ax2.set_yticks([0, 1, 2, 3, 4, 5])
    ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], trialNo)

    ax3.plot(efficHazel, label='Hazelnut')
    ax3.plot(efficPeanut, label='Peanut')
    ax3.legend()
    ax3.set_xlabel('Trial number')
    ax3.set_ylabel('Net efficiency')
    ax3.set_yticks([0, 1, 2, 3, 4, 5])
    ax3.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], trialNo)
    plt.show()

userChoice = input(
    "\n  Input the number of the variable you wish to change:"
    " \n (1. Energy gain) \n (2. Search time) \n (3. Handling time) \n (4. Energy used searching) \n"
    " (5. Energy used handling) \n")

if userChoice == "1":
    userStart = input("\n Input the number of the nut you wish to change"
                      " the energy gain of: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        gainPeanut = int(input("How many Kcals does the squirrel gain from eating a peanut?: "))

        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        grossPeanut = (gainPeanut / usedPeanut)
        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        plot()

    print()
    if userStart == "2":
        gainHazel = int(input("How many Kcals does the squirrel gain from eating a hazelnut?: "))

        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)
        grossHazel = (gainHazel / usedHazel)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)
        plot()

if userChoice == "2":
    userStart = input("\n Input the number of the nut you wish to change"
                        " the search time of: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        userPeanut = int(input("How many seconds does it take the squirrel to find the peanut?: "))
        searchPeanut = np.linspace(userPeanut, userPeanut, num=10)

        usedPeanut = searchPeanut + handlePeanut
        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        grossPeanut = (gainPeanut / usedPeanut)
        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        plot()

    if userStart == "2":
        userHazel = int(input("How many seconds does it take the squirrel to find the hazelnut? "
                              "(Search time will continue to increase by "
                          "the value you input for each subsequent trial): "))
        searchHazel = np.linspace(userHazel, (userHazel*10), num=10)
        usedHazel = searchHazel + handleHazel
        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)
        grossHazel = (gainHazel / usedHazel)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)
        plot()

if userChoice == "3":
    userStart = input("\n Input the number of the nut you wish to change"
                              " the handling time for: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        handlePeanut = int(input("How many seconds does it take the squirrel to handle the peanut?: "))
        usedPeanut = searchPeanut + handlePeanut
        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        grossPeanut = (gainPeanut / usedPeanut)
        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        plot()

    print()
    if userStart == "2":
        handleHazel = int(input("How many seconds does it take the squirrel to handle the hazelnut?: "))
        usedHazel = searchHazel + handleHazel
        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)
        grossHazel = (gainHazel / usedHazel)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)
        plot()

if userChoice == "4":
    userStart = input("\n Input the number of the nut you wish to change"
                              " the energy used searching for: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        userPeanut = int(input("How many Kcals does the squirrel use to find the peanut?: "))
        usedPeanut = np.linspace((userPeanut + 2), (userPeanut + 2), num=10)
        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        grossPeanut = (gainPeanut / usedPeanut)
        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        plot()

    print()
    if userStart == "2":
        userHazel = int(input("How many Kcals does the squirrel use to find the hazelnut?: "))
        usedHazel = np.linspace((userHazel + 1), (userHazel + 10), num=10)
        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)
        grossHazel = (gainHazel / usedHazel)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)
        plot()


if userChoice == "5":
    userStart = input("\n Input the number of the nut you wish to change"
                              " the energy used handling for: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        userPeanut = int(input("How many Kcals does the squirrel use to handle the peanut?: "))
        usedPeanut = np.linspace((userPeanut+1), (userPeanut+1), num=10)
        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        grossPeanut = (gainPeanut / usedPeanut)
        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        plot()

    if userStart == "2":
        userHazel = int(input("How many Kcals does the squirrel use to handle the hazelnut?: "))
        usedHazel = np.linspace((userHazel+1), (userHazel+10), num=10)
        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)
        grossHazel = (gainHazel / usedHazel)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)
        plot()

