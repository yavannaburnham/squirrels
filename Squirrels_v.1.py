import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


print("\033[1m" + "Optimal Diet Model Practice" "\033[0m")
print()
print("This is a very simple model where net rate is calculated as Kcal gained / handling time + search time.")
print()
print("In this scenario, the squirrel can choose one of two food items:")
print()
hazelnut = 9
print("Hazelnut Kcal:", hazelnut)
print()
peanut = 5
print("Peanut Kcal:", peanut)
print()
print("It takes the squirrel 1 second to handle a hazelnut. "
      "The squirrel loses 1 calorie for every second it spends handling an item.")
print()
a = 1
print("Handling time hazelnut (seconds):", a)
print()
print("It takes the squirrel 2 seconds to handle a peanut. ")
print()
b = 2
print("Handling time peanut (seconds):", b)
print()
print("It always takes the squirrel 1 second to find the peanut. "
      "The squirrel loses 1 calorie for every second it spends searching for an item.")
print()
c = 1
print("Search time peanut (seconds):", c)
print()
print("Search time for the hazelnut is variable."
      " In the first trial this takes 1 second (the same as for a peanut),"
      " but with each subsequent trial search time is increased by 1 second.")
print()
d = np.arange(1, 11, 1)
print("Search time hazelnut (seconds):", d)
print()
e = peanut / (b + c)
print("Net rate - peanut (kcal per second): ", e)
print()
f = hazelnut / (a + d)
print("Net rate - hazelnut (kcal per second): ", f)
print()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #Generate trial numbers
y = [1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7]  #Constant net value peanut (Kcal / second) for graph

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(y, label='Peanut')
ax.plot(f, label='Hazelnut')
ax.set_xlabel('Trial number')
ax.set_ylabel('Net rate (Kcal / second)')
ax.legend()
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], d)
ax.set_yticks([0, 1, 2, 3, 4, 5])
plt.show()