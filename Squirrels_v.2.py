import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print("\033[1m" + "Net Rate" "\033[0m")
print()
print("Energy gain - Energy used) / (Search time + Handling time")
print()
print("Peanut:")
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
print()
netratePeanut = (gainPeanut - usedPeanut) / (searchPeanut + handlePeanut)
print()
print("Net rate for a peanut (kcal / s):", netratePeanut)
print()
print()
print("Hazelnut:")
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
print("Net rate for a hazelnut (kcal / s):", netrateHazel)

netratecPeanut = [0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67, 0.67]  #Constant net value peanut (Kcal / second) for graph

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(netrateHazel, label='Hazelnut')
ax.plot(netratecPeanut, label='Peanut')
ax.set_xlabel('Trial number')
ax.set_ylabel('Net rate')
ax.legend()
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
ax.set_yticks([0, 1, 2, 3, 4, 5])
plt.show()

print()
print()
print("\033[1m" + "Gross Efficiency" "\033[0m")
print()
print("Energy gain) / (Energy used searching + Energy used handling")
grossPeanut = (gainPeanut / usedPeanut)
print()
print("Gross Efficiency Peanut:", grossPeanut)
grossHazel = (gainHazel / usedHazel)
print()
print("Gross Efficiency Hazelnut:", grossHazel)

grosscPeanut = [1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67]  #Constant gross efficiency for peanut for graph

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(grossHazel, label='Hazelnut')
ax.plot(grosscPeanut, label='Peanut')
ax.set_xlabel('Trial number')
ax.set_ylabel('Gross Efficiency')
ax.legend()
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
ax.set_yticks([0, 1, 2, 3, 4, 5])
plt.show()

print()
print()
print("\033[1m" + "Net Efficiency" "\033[0m")
print()
print("Energy gain - Energy used searching - Energy used handling) / (Energy used searching + Energy used handling)")
efficPeanut = (gainPeanut - usedPeanut) / (usedPeanut)
print()
print("Net Efficiency Peanut:", efficPeanut)
print()
efficHazel = (gainHazel - usedHazel) / (usedHazel)
print()
print("Net Efficiency Hazelnut:", efficHazel)
efficcPeanut = [1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67]  #Constant net efficiency for peanut for graph

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(efficHazel, label='Hazelnut')
ax.plot(efficcPeanut, label='Peanut')
ax.set_xlabel('Trial number')
ax.set_ylabel('Net Efficiency')
ax.legend()
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], searchHazel)
ax.set_yticks([0, 1, 2, 3, 4, 5])
plt.show()
