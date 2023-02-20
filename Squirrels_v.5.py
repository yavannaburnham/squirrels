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

userChoice = input(
    "\n  Input the number of the variable you wish to change:"
    " \n (1. Energy gain) \n (2. Handling time) \n (3. Search time) \n ")

if userChoice == "1":
    userStart = input("\n Input the number of the nut you wish to change"
                      " the energetic gain of: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        gainPeanut = int(input("How many Kcals does the squirrel gain from eating a peanut?: "))

        usedPeanut = searchPeanut + handlePeanut
        usedHazel = searchHazel + handleHazel

        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)

        grossPeanut = (gainPeanut / usedPeanut)
        grossHazel = (gainHazel / usedHazel)

        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)

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

    print()
    if userStart == "2":
        gainHazel = int(input("How many Kcals does the squirrel gain from eating a hazelnut?: "))

        usedPeanut = searchPeanut + handlePeanut
        usedHazel = searchHazel + handleHazel

        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)

        grossPeanut = (gainPeanut / usedPeanut)
        grossHazel = (gainHazel / usedHazel)

        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)

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

if userChoice == "2":
    userStart = input("\n Input the number of the nut you wish to change"
                      " the handling time for: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        handlePeanut = int(input("How many seconds does it take a squirrel to handle a peanut?: "))

        usedPeanut = searchPeanut + handlePeanut
        usedHazel = searchHazel + handleHazel

        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)

        grossPeanut = (gainPeanut / usedPeanut)
        grossHazel = (gainHazel / usedHazel)

        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)

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

    print()
    if userStart == "2":
        handleHazel = int(input("How many seconds does it take a squirrel to handle a hazelnut?: "))

        usedPeanut = searchPeanut + handlePeanut
        usedHazel = searchHazel + handleHazel

        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)

        grossPeanut = (gainPeanut / usedPeanut)
        grossHazel = (gainHazel / usedHazel)

        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)

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

if userChoice == "3":
    userStart = input("\n Input the number of the nut you wish to change"
                              " the search time for: \n (1. Peanut) \n (2. Hazelnut)")
    print()
    if userStart == "1":
        userPeanut = int(input("How many seconds does it take a squirrel to find a peanut?: "))
        searchPeanut = np.linspace(userPeanut, userPeanut, num=10)

        usedPeanut = searchPeanut + handlePeanut
        usedHazel = searchHazel + handleHazel

        netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
        netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)

        grossPeanut = (gainPeanut / usedPeanut)
        grossHazel = (gainHazel / usedHazel)

        efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
        efficHazel = (gainHazel - usedHazel) / (usedHazel)

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

print()
if userStart == "2":
    userHazel = int(input("How many seconds does it take a squirrel "
                                  "to find a hazelnut (this will continue to increase by "
                          "the value you input for each subsequent trial)?: "))

    searchHazel = np.linspace(userHazel, (userHazel * 10), num=10)

    usedPeanut = searchPeanut + handlePeanut
    usedHazel = searchHazel + handleHazel

    netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
    netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)

    grossPeanut = (gainPeanut / usedPeanut)
    grossHazel = (gainHazel / usedHazel)

    efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
    efficHazel = (gainHazel - usedHazel) / (usedHazel)

    trialNo = np.linspace(1, 10, num=10)

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
