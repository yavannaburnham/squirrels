import numpy as np
import matplotlib.pyplot as plt

print("Three currencies are modelled: net rate, gross efficiency, and net efficiency.")
print()
print("1. Net rate")
print("2. Gross efficiency")
print("3. Net efficiency")
print("4. Compare all currencies")

gainPeanut = 5
gainHazel = 9

searchPeanut = np.linspace(1, 1, num=10)
searchHazel = np.linspace(1, 10, num=10)

handlePeanut = 2
handleHazel = 1

usedPeanut = searchPeanut + handlePeanut
usedHazel = searchHazel + handleHazel

netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)

grossPeanut = (gainPeanut / usedPeanut)
grossHazel = (gainHazel / usedHazel)

efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
efficHazel = (gainHazel - usedHazel) / (usedHazel)

lang = input("Type the number of the model you would like to run: ")
print()
match lang:
      case "1":
            print("\033[1m" + "Net Rate" "\033[0m")
            print()
            print("Energy gain - Energy used) / (Search time + Handling time)")


            fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
            ax.plot(netrateHazel, label='Hazelnut')
            ax.plot(netratePeanut, label='Peanut')
            ax.set_xlabel('Trial number')
            ax.set_ylabel('Net rate')
            ax.legend()
            ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
            ax.set_yticks([0, 1, 2, 3, 4, 5])
            plt.show()

      case "2":
            print("\033[1m" + "Gross Efficiency" "\033[0m")
            print()
            print("(Energy gain) / (Energy used searching + Energy used handling)")

            fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
            ax.plot(grossHazel, label='Hazelnut')
            ax.plot(grossPeanut, label='Peanut')
            ax.set_xlabel('Trial number')
            ax.set_ylabel('Gross Efficiency')
            ax.legend()
            ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
            ax.set_yticks([0, 1, 2, 3, 4, 5])
            plt.show()

      case "3":
            print("\033[1m" + "Net Efficiency" "\033[0m")
            print()
            print("(Energy gain - Energy used searching - Energy used handling) / (Energy used searching + Energy used handling)")

            fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
            ax.plot(efficHazel, label='Hazelnut')
            ax.plot(efficPeanut, label='Peanut')
            ax.set_xlabel('Trial number')
            ax.set_ylabel('Net Efficiency')
            ax.legend()
            ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
            ax.set_yticks([0, 1, 2, 3, 4, 5])
            plt.show()

      case "4":
            print("\033[1m" + "Compare all Currencies" "\033[0m")

            fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
            fig.suptitle('Currency Comparison')

            ax1.plot(netrateHazel, label='Hazelnut')
            ax1.plot(netratePeanut, label='Peanut')
            ax1.legend()
            ax1.set_xlabel('Trial number')
            ax1.set_ylabel('Net rate')
            ax1.set_yticks([0, 1, 2, 3, 4, 5])
            ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)

            ax2.plot(grossHazel, label='Hazelnut')
            ax2.plot(grossPeanut, label='Peanut')
            ax2.legend()
            ax2.set_xlabel('Trial number')
            ax2.set_ylabel('Gross efficiency')
            ax2.set_yticks([0, 1, 2, 3, 4, 5])
            ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)

            ax3.plot(efficHazel, label='Hazelnut')
            ax3.plot(efficPeanut, label='Peanut')
            ax3.legend()
            ax3.set_xlabel('Trial number')
            ax3.set_ylabel('Net efficiency')
            ax3.set_yticks([0, 1, 2, 3, 4, 5])
            ax3.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
            plt.show()