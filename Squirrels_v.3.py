import numpy as np
import matplotlib.pyplot as plt

print("Three currencies are modelled: net rate, gross efficiency, and net efficiency.")
print()
print("1. Net rate")
print("2. Gross efficiency")
print("3. Net efficiency")
print("4. Compare all currencies")
print()

lang = input("Type the number of the model you would like to run: ")
print()
match lang:
      case "1":
            print("\033[1m" + "Net Rate" "\033[0m")
            print()
            print("Energy gain - Energy used) / (Search time + Handling time)")
            print()
            gainPeanut = 5
            print("Energy gained from eating peanut (Kcal):", gainPeanut)
            print()
            print("It always takes the squirrel 1 second to find the peanut and 2 seconds to eat it. "
                  "The squirrel uses 1 calorie per second of search / handling time.")
            print()
            searchPeanut = 1
            print("Search time for a peanut (s):", searchPeanut)
            print()
            handlePeanut = 2
            print("Handling time for a peanut (s):", handlePeanut)
            print()
            usedPeanut = searchPeanut + handlePeanut
            print("Energy used to obtain peanut (kcal):", usedPeanut)
            netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
            print()
            print("Net rate for a peanut:", netratePeanut)
            print()
            gainHazel = 9
            print("Energy gained from eating hazelnut (kcal):", gainHazel)
            print()
            print("Search time for the hazelnut is variable."
                  " In the first trial this takes 1 second (the same as for a peanut),"
                  " but with each subsequent trial search time is increased by 1 second.")
            print()
            searchHazel = np.linspace(1, 10, num=10)
            print("Search time for a hazelnut (s):", searchHazel)
            print()
            print("It always takes a squirrel 1 second to handle a hazelnut")
            handleHazel = 1
            print()
            print("Handling time for a hazelnut (s):", handleHazel)
            print()
            usedHazel = searchHazel + handleHazel
            print("Energy used to obtain hazelnut (kcal):", usedHazel)
            netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)
            print()
            print("Net rate for a hazelnut:", netrateHazel)

            netratecPeanut = [0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67,
                              0.67]  # Constant net value peanut (Kcal / second) for graph

            fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
            ax.plot(netrateHazel, label='Hazelnut')
            ax.plot(netratecPeanut, label='Peanut')
            ax.set_xlabel('Trial number')
            ax.set_ylabel('Net rate')
            ax.legend()
            ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
            ax.set_yticks([0, 1, 2, 3, 4, 5])
            plt.show()


      case "2":
            print("\033[1m" + "Gross Efficiency" "\033[0m")
            print()
            print("(Energy gain) / (Energy used searching + Energy used handling")
            print()
            gainPeanut = 5
            print("Energy gained from eating peanut (Kcal):", gainPeanut)
            print()
            print("It always takes the squirrel 1 second to find the peanut and 2 seconds to eat it. "
                  "The squirrel uses 1 calorie per second of search / handling time.")
            print()
            searchPeanut = 1
            print("Search time for a peanut (s):", searchPeanut)
            print()
            handlePeanut = 2
            print("Handling time for a peanut (s):", handlePeanut)
            print()
            usedPeanut = searchPeanut + handlePeanut
            print("Energy used to obtain peanut (kcal):", usedPeanut)
            grossPeanut = (gainPeanut / usedPeanut)
            print()
            print("Gross Efficiency Peanut:", grossPeanut)
            print()
            gainHazel = 9
            print("Energy gained from eating hazelnut (kcal):", gainHazel)
            print()
            print("Search time for the hazelnut is variable."
                  " In the first trial this takes 1 second (the same as for a peanut),"
                  " but with each subsequent trial search time is increased by 1 second.")
            print()
            searchHazel = np.linspace(1, 10, num=10)
            print("Search time for a hazelnut (s):", searchHazel)
            print()
            print("It always takes a squirrel 1 second to handle a hazelnut")
            handleHazel = 1
            print()
            print("Handling time for a hazelnut (s):", handleHazel)
            print()
            usedHazel = searchHazel + handleHazel
            print("Energy used to obtain hazelnut (kcal):", usedHazel)
            grossHazel = (gainHazel / usedHazel)
            print()
            print("Gross Efficiency Hazelnut:", grossHazel)
            grosscPeanut = [1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67,
                            1.67]  # Constant gross efficiency for peanut for graph

            fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
            ax.plot(grossHazel, label='Hazelnut')
            ax.plot(grosscPeanut, label='Peanut')
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
            gainPeanut = 5
            print("Energy gained from eating peanut (Kcal):", gainPeanut)
            print()
            print("It always takes the squirrel 1 second to find the peanut and 2 seconds to eat it. "
                  "The squirrel uses 1 calorie per second of search / handling time.")
            print()
            searchPeanut = 1
            print("Search time for a peanut (s):", searchPeanut)
            print()
            handlePeanut = 2
            print("Handling time for a peanut (s):", handlePeanut)
            print()
            usedPeanut = searchPeanut + handlePeanut
            print("Energy used to obtain peanut (kcal):", usedPeanut)
            efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
            print()
            print("Net Efficiency Peanut:", efficPeanut)
            print()
            gainHazel = 9
            print("Energy gained from eating hazelnut (kcal):", gainHazel)
            print()
            print("Search time for the hazelnut is variable."
                  " In the first trial this takes 1 second (the same as for a peanut),"
                  " but with each subsequent trial search time is increased by 1 second.")
            print()
            searchHazel = np.linspace(1, 10, num=10)
            print("Search time for a hazelnut (s):", searchHazel)
            print()
            print("It always takes a squirrel 1 second to handle a hazelnut")
            handleHazel = 1
            print()
            print("Handling time for a hazelnut (s):", handleHazel)
            print()
            usedHazel = searchHazel + handleHazel
            print("Energy used to obtain hazelnut (kcal):", usedHazel)
            efficHazel = (gainHazel - usedHazel) / (usedHazel)
            print()
            print("Net Efficiency Hazelnut:", efficHazel)
            efficcPeanut = [1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67,
                            1.67]  # Constant net efficiency for peanut for graph

            fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
            ax.plot(efficHazel, label='Hazelnut')
            ax.plot(efficcPeanut, label='Peanut')
            ax.set_xlabel('Trial number')
            ax.set_ylabel('Net Efficiency')
            ax.legend()
            ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
            ax.set_yticks([0, 1, 2, 3, 4, 5])
            plt.show()

      case "4":
            print("\033[1m" + "Compare all Currencies" "\033[0m")

            # Net rate
            gainPeanut = 5
            searchPeanut = 1
            handlePeanut = 2
            usedPeanut = searchPeanut + handlePeanut
            netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
            gainHazel = 9
            searchHazel = np.linspace(1, 10, num=10)
            handleHazel = 1
            usedHazel = searchHazel + handleHazel
            netrateHazel = (gainHazel - usedHazel) / (searchHazel + handleHazel)
            netratecPeanut = [0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67,
                              0.67]  # Constant net value peanut

            # Gross efficiency
            grossPeanut = (gainPeanut / usedPeanut)
            grossHazel = (gainHazel / usedHazel)
            grosscPeanut = [1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67]

            # Net efficiency
            efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
            efficHazel = (gainHazel - usedHazel) / (usedHazel)
            efficcPeanut = [1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67]

            fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
            fig.suptitle('Currency Comparison')

            ax1.plot(netrateHazel, label='Hazelnut')
            ax1.plot(netratecPeanut, label='Peanut')
            ax1.legend()
            ax1.set_xlabel('Trial number')
            ax1.set_ylabel('Net rate')
            ax1.set_yticks([0, 1, 2, 3, 4, 5])
            ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)

            ax2.plot(grossHazel, label='Hazelnut')
            ax2.plot(grosscPeanut, label='Peanut')
            ax2.legend()
            ax2.set_xlabel('Trial number')
            ax2.set_ylabel('Gross efficiency')
            ax2.set_yticks([0, 1, 2, 3, 4, 5])
            ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)


            ax3.plot(efficHazel, label='Hazelnut')
            ax3.plot(efficcPeanut, label='Peanut')
            ax3.legend()
            ax3.set_xlabel('Trial number')
            ax3.set_ylabel('Net efficiency')
            ax3.set_yticks([0, 1, 2, 3, 4, 5])
            ax3.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
            plt.show()

