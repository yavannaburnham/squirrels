import numpy as np
import matplotlib.pyplot as plt

# Set baseline values
GainPeanut = np.linspace(3, 8, num=10)
GainHazel = np.linspace(7, 12, num=10)
SearchTimePeanut = np.linspace(1, 1, num=10)
SearchTimeHazel = np.linspace(4, 4, num=10)
HandleTimePeanut = np.linspace(2, 2, num=10)
HandleTimeHazel = np.linspace(1, 1, num=10)
SearchEnergyPeanut = np.linspace(1, 1, num=10)
SearchEnergyHazel = np.linspace(4, 4, num=10)
HandleEnergyPeanut = np.linspace(2, 2, num=10)
HandleEnergyHazel = np.linspace(1, 1, num=10)


# Define currencies
def currencies(Gain, SearchEnergy, HandleEnergy, SearchTime, HandleTime):
    NetRate = (Gain - SearchEnergy - HandleEnergy) / (SearchTime + HandleTime)
    NetEfficiency = (Gain - SearchEnergy - HandleEnergy) / (SearchEnergy + HandleEnergy)
    GrossRate = (Gain / (SearchTime + HandleTime))
    GrossEfficiency = (Gain / (SearchEnergy + HandleEnergy))
    return [NetRate, NetEfficiency, GrossRate, GrossEfficiency]


PeanutOutput = currencies(GainPeanut, SearchEnergyPeanut, HandleEnergyPeanut, SearchTimePeanut, HandleTimePeanut)
NetRatePeanut = PeanutOutput[0]
NetEfficiencyPeanut = PeanutOutput[1]
GrossRatePeanut = PeanutOutput[2]
GrossEfficiencyPeanut = PeanutOutput[3]

HazelOutput = currencies(GainHazel, SearchEnergyHazel, HandleEnergyHazel, SearchTimeHazel, HandleTimeHazel)
NetRateHazel = HazelOutput[0]
NetEfficiencyHazel = HazelOutput[1]
GrossRateHazel = HazelOutput[2]
GrossEfficiencyHazel = HazelOutput[3]


var_choice = input("Change 'Energy gain', 'Search time' or 'Handling time'?: ")
if var_choice =='Energy gain':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")
    if nut_choice == 'p':
        minGainPeanut = float(input("Enter minimum energy gain for peanuts: "))
        maxGainPeanut = float(input("Enter maximum energy gain for peanuts: "))
        print("Kcal gained ranges between {} and {}".format(minGainPeanut, maxGainPeanut))
        GainPeanut = np.linspace(minGainPeanut, maxGainPeanut, num=10)
        xaxis = GainPeanut

    if nut_choice == 'h':
        minGainHazel = float(input("Enter minimum energy gain for hazelnuts (kcal): "))
        maxGainHazel = float(input("Enter maximum energy gain for hazelnuts (kcal): "))
        print("Energy gained ranges between {} and {} Kcals".format(minGainHazel, maxGainHazel))
        GainHazel = np.linspace(minGainHazel, maxGainHazel, num=10)
        xaxis = GainHazel

if var_choice == 'Search time':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")
    if nut_choice == 'p':
        minSearchPeanut = float(input("Enter minimum search time for peanuts (s): "))
        maxSearchPeanut = float(input("Enter maximum search time for peanuts (s): "))
        print("Search time ranges between {} and {} seconds".format(minSearchPeanut, maxSearchPeanut))
        SearchTimePeanut = np.linspace(minSearchPeanut, maxSearchPeanut, num=10)
        xaxis = SearchTimePeanut

    if nut_choice == 'h':
        minSearchHazel = float(input("Enter minimum search time for hazelnuts (s): "))
        maxSearchHazel = float(input("Enter maximum search time for hazelnuts (s): "))
        print("Search time ranges between {} and {} seconds".format(minSearchHazel, maxSearchHazel))
        SearchTimeHazel = np.linspace(minSearchHazel, maxSearchHazel, num=10)
        xaxis = SearchTimeHazel

if var_choice == 'Handling time':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")
    if nut_choice == 'p':
        minHandlePeanut = float(input("Enter minimum handling time for peanuts (s): "))
        maxHandlePeanut = float(input("Enter maximum handling time for peanuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(minHandlePeanut, maxHandlePeanut))
        HandleTimePeanut = np.linspace(minHandlePeanut, maxHandlePeanut, num=10)
        xaxis = HandleTimePeanut

    if nut_choice == 'h':
        minHandleHazel = float(input("Enter minimum handling time for hazelnuts (s): "))
        maxHandleHazel = float(input("Enter maximum handling time for hazelnuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(minHandleHazel, maxHandleHazel))
        HandleTimeHazel = np.linspace(minHandleHazel, maxHandleHazel, num=10)
        xaxis = HandleTimeHazel


PeanutOutput = currencies(GainPeanut, SearchEnergyPeanut, HandleEnergyPeanut, SearchTimePeanut, HandleTimePeanut)
NetRatePeanut = PeanutOutput[0]
NetEfficiencyPeanut = PeanutOutput[1]
GrossRatePeanut = PeanutOutput[2]
GrossEfficiencyPeanut = PeanutOutput[3]

HazelOutput = currencies(GainHazel, SearchEnergyHazel, HandleEnergyHazel, SearchTimeHazel, HandleTimeHazel)
NetRateHazel = HazelOutput[0]
NetEfficiencyHazel = HazelOutput[1]
GrossRateHazel = HazelOutput[2]
GrossEfficiencyHazel = HazelOutput[3]

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Currency Comparison')
ax1.plot(xaxis, NetRateHazel, label='Hazelnut')
ax1.plot(xaxis, NetRatePeanut, label='Peanut')
ax1.legend()
ax1.set_xlabel(var_choice)
ax1.set_ylabel('Net rate')

ax2.plot(xaxis, NetEfficiencyHazel,label='Hazelnut')
ax2.plot(xaxis, NetEfficiencyPeanut,label='Peanut')
ax2.legend()
ax2.set_xlabel(var_choice)
ax2.set_ylabel('Net efficiency')


ax3.plot(xaxis, GrossRateHazel,label='Hazelnut')
ax3.plot(xaxis, GrossRatePeanut,label='Peanut')
ax3.legend()
ax3.set_xlabel(var_choice)
ax3.set_ylabel('Gross rate')


ax4.plot(xaxis, GrossEfficiencyHazel,label='Hazelnut')
ax4.plot(xaxis, GrossEfficiencyPeanut,label='Peanut')
ax4.legend()
ax4.set_xlabel(var_choice)
ax4.set_ylabel('Gross efficiency')
plt.show()

intercept_found = False
for i in range(len(GainPeanut) - 1):
    if NetRatePeanut[i] <= NetRateHazel[i] and NetRatePeanut[i + 1] >= NetRateHazel[i + 1] or NetRatePeanut[i] >= NetRateHazel[i] and NetRatePeanut[i + 1] <= NetRateHazel[i + 1]:
        slope1 = (NetRatePeanut[i + 1] - NetRatePeanut[i]) / (GainPeanut[i + 1] - GainPeanut[i])
        slope2 = (NetRateHazel[i + 1] - NetRateHazel[i]) / (GainPeanut[i + 1] - GainPeanut[i])

        x_intersect = (NetRateHazel[i] - NetRatePeanut[i] + slope1 * GainPeanut[i] - slope2 * GainPeanut[i]) / (slope1 - slope2)
        print(f"The crossover point is: {x_intersect:.2f}")
