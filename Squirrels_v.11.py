import numpy as np
import matplotlib.pyplot as plt


# Set baseline values
gain_peanut = np.linspace(3, 3, num=10)
gain_hazel = np.linspace(7, 7, num=10)
search_time_peanut = np.linspace(1, 1, num=10)
search_time_hazel = np.linspace(4, 4, num=10)
handle_time_peanut = np.linspace(2, 2, num=10)
handle_time_hazel = np.linspace(1, 1, num=10)
search_energy_peanut = np.linspace(1, 1, num=10)
search_energy_hazel = np.linspace(4, 4, num=10)
handle_energy_peanut = np.linspace(2, 2, num=10)
handle_energy_hazel = np.linspace(1, 1, num=10)
x_axis = gain_peanut
var_label = "Energy gain"


# Define currencies
def currencies(gain, search_energy, handle_energy, search_time, handle_time):
    net_rate = (gain - search_energy - handle_energy) / (search_time + handle_time)
    net_efficiency = (gain - search_energy - handle_energy) / (search_energy + handle_energy)
    gross_rate = (gain / (search_time + handle_time))
    gross_efficiency = (gain / (search_energy + handle_energy))
    return [net_rate, net_efficiency, gross_rate, gross_efficiency]


var_choice = input("Enter '1' for energy gain, '2' for search time, '3' for handling time, '4' for search energy,"
                   " or '5' for handling energy: ")
if var_choice == '1':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_gain_peanut = float(input("Enter minimum energy gain for peanuts: "))
        max_gain_peanut = float(input("Enter maximum energy gain for peanuts: "))
        print("Kcal gained ranges between {} and {}".format(min_gain_peanut, max_gain_peanut))
        gain_peanut = np.linspace(min_gain_peanut, max_gain_peanut, num=10)
        x_axis = gain_peanut
        var_label = "Energy gain"

    if nut_choice == 'h':
        min_gain_hazel = float(input("Enter minimum energy gain for hazelnuts (Kcal): "))
        max_gain_hazel = float(input("Enter maximum energy gain for hazelnuts (Kcal): "))
        print("Energy gained ranges between {} and {} calories".format(min_gain_hazel, max_gain_hazel))
        gain_hazel = np.linspace(min_gain_hazel, max_gain_hazel, num=10)
        x_axis = gain_hazel
        var_label = "Energy gain"


if var_choice == '2':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_search_time_peanut = float(input("Enter minimum search time for peanuts (s): "))
        max_search_time_peanut = float(input("Enter maximum search time for peanuts (s): "))
        print("Search time ranges between {} and {} seconds".format(min_search_time_peanut, max_search_time_peanut))
        search_time_peanut = np.linspace(min_search_time_peanut, max_search_time_peanut, num=10)
        x_axis = search_time_peanut
        var_label = "Search time"

    if nut_choice == 'h':
        min_search_time_hazel = float(input("Enter minimum search time for hazelnuts (s): "))
        max_search_time_hazel = float(input("Enter maximum search time for hazelnuts (s): "))
        print("Search time ranges between {} and {} seconds".format(min_search_time_hazel, max_search_time_hazel))
        search_time_hazel = np.linspace(min_search_time_hazel, max_search_time_hazel, num=10)
        x_axis = search_time_hazel
        var_label = "Search time"


if var_choice == '3':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_handle_time_peanut = float(input("Enter minimum handling time for peanuts (s): "))
        max_handle_time_peanut = float(input("Enter maximum handling time for peanuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(min_handle_time_peanut, max_handle_time_peanut))
        handle_time_peanut = np.linspace(min_handle_time_peanut, max_handle_time_peanut, num=10)
        x_axis = handle_time_peanut
        var_label = "Handling time"

    if nut_choice == 'h':
        min_handle_time_hazel = float(input("Enter minimum handling time for hazelnuts (s): "))
        max_handle_time_hazel = float(input("Enter maximum handling time for hazelnuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(min_handle_time_hazel, max_handle_time_hazel))
        handle_time_hazel = np.linspace(min_handle_time_hazel, max_handle_time_hazel, num=10)
        x_axis = handle_time_hazel
        var_label = "Handling time"

if var_choice == '4':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_search_energy_peanut = float(input("Enter minimum energy used to search for peanuts (Kcal): "))
        max_search_energy_peanut = float(input("Enter maximum energy used to search for peanuts (Kcal): "))
        print("Search energy ranges between {} and {} calories".format(min_search_energy_peanut,
                                                                       max_search_energy_peanut))
        search_energy_peanut = np.linspace(min_search_energy_peanut, max_search_energy_peanut, num=10)
        x_axis = search_energy_peanut
        var_label = "Search energy"

    if nut_choice == 'h':
        min_search_energy_hazel = float(input("Enter minimum energy used to search for hazelnuts (Kcal): "))
        max_search_energy_hazel = float(input("Enter maximum energy used to search for hazelnuts (Kcal): "))
        print("Search energy ranges between {} and {} calories".format(min_search_energy_hazel,
                                                                       max_search_energy_hazel))
        search_energy_hazel = np.linspace(min_search_energy_hazel, max_search_energy_hazel, num=10)
        x_axis = search_energy_hazel
        var_label = "Search energy"

if var_choice == '5':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_handle_energy_peanut = float(input("Enter minimum energy used to handle peanuts (Kcal): "))
        max_handle_energy_peanut = float(input("Enter maximum energy used to handle peanuts (Kcal): "))
        print("Handling energy ranges between {} and {} calories".format(min_handle_energy_peanut,
                                                                         max_handle_energy_peanut))
        handle_energy_peanut = np.linspace(min_handle_energy_peanut, max_handle_energy_peanut, num=10)
        x_axis = handle_energy_peanut
        var_label = "Handling energy"

    if nut_choice == 'h':
        min_handle_energy_hazel = float(input("Enter minimum energy used to handle hazelnuts (Kcal): "))
        max_handle_energy_hazel = float(input("Enter maximum energy used to handle hazelnuts (Kcal): "))
        print("Handling energy ranges between {} and {} calories".format(min_handle_energy_hazel,
                                                                         max_handle_energy_hazel))
        handle_energy_hazel = np.linspace(min_handle_energy_hazel, max_handle_energy_hazel, num=10)
        x_axis = handle_energy_hazel
        var_label = "Handling energy"

peanut_output = currencies(gain_peanut, search_energy_peanut, handle_energy_peanut, search_time_peanut,
                           handle_time_peanut)
net_rate_peanut = peanut_output[0]
net_efficiency_peanut = peanut_output[1]
gross_rate_peanut = peanut_output[2]
gross_efficiency_peanut = peanut_output[3]


hazel_output = currencies(gain_hazel, search_energy_hazel, handle_energy_hazel, search_time_hazel, handle_time_hazel)
net_rate_hazel = hazel_output[0]
net_efficiency_hazel = hazel_output[1]
gross_rate_hazel = hazel_output[2]
gross_efficiency_hazel = hazel_output[3]

# Plot currencies
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Currency Comparison')
ax1.plot(x_axis, net_rate_hazel, label='Hazelnut')
ax1.plot(x_axis, net_rate_peanut, label='Peanut')
ax1.legend()
ax1.set_xlabel(var_label)
ax1.set_ylabel('Net rate')

ax2.plot(x_axis, net_efficiency_hazel, label='Hazelnut')
ax2.plot(x_axis, net_efficiency_peanut, label='Peanut')
ax2.legend()
ax2.set_xlabel(var_label)
ax2.set_ylabel('Net efficiency')

ax3.plot(x_axis, gross_rate_hazel, label='Hazelnut')
ax3.plot(x_axis, gross_rate_peanut, label='Peanut')
ax3.legend()
ax3.set_xlabel(var_label)
ax3.set_ylabel('Gross rate')

ax4.plot(x_axis, gross_efficiency_hazel, label='Hazelnut')
ax4.plot(x_axis, gross_efficiency_peanut, label='Peanut')
ax4.legend()
ax4.set_xlabel(var_label)
ax4.set_ylabel('Gross efficiency')
plt.show()

# Create an empty list to store results of comparison
result = []

# Iterate over each value in both net rates and compare them using a loop
for i in range(len(x_axis)):
    if net_rate_hazel[i] > net_rate_peanut[i]:
        result.append(1)
    else:
        result.append(0)

# Find index in 'result' where 0 becomes 1 or vice versa
cross_over_point = None
for i in range(1, len(result)):
    if result[i] != result[i-1]:
        cross_over_point = i
        break

# Scale the cross-over point to the chosen variable
if cross_over_point is not None:
    print(f"The cross-over point for net rate is approximately at: {x_axis[cross_over_point]:.1f}")
else:
    print("No cross-over point for net rate found.")
