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


# Define currencies
def currencies(gain, search_energy, handle_energy, search_time, handle_time):
    net_rate = (gain - search_energy - handle_energy) / (search_time + handle_time)
    net_efficiency = (gain - search_energy - handle_energy) / (search_energy + handle_energy)
    gross_rate = (gain / (search_time + handle_time))
    gross_efficiency = (gain / (search_energy + handle_energy))
    return [net_rate, net_efficiency, gross_rate, gross_efficiency]


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


var_choice = input("Change 'Energy gain', 'Search time', 'Handling time', 'Search energy',"
                   " or 'Handling energy'?: ")
if var_choice == 'Energy gain':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_gain_peanut = float(input("Enter minimum energy gain for peanuts: "))
        max_gain_peanut = float(input("Enter maximum energy gain for peanuts: "))
        print("Kcal gained ranges between {} and {}".format(min_gain_peanut, max_gain_peanut))
        gain_peanut = np.linspace(min_gain_peanut, max_gain_peanut, num=10)
        x_axis = gain_peanut

    if nut_choice == 'h':
        min_gain_hazel = float(input("Enter minimum energy gain for hazelnuts (Kcal): "))
        max_gain_hazel = float(input("Enter maximum energy gain for hazelnuts (Kcal): "))
        print("Energy gained ranges between {} and {} calories".format(min_gain_hazel, max_gain_hazel))
        GainHazel = np.linspace(min_gain_hazel, max_gain_hazel, num=10)
        x_axis = gain_hazel


if var_choice == 'Search time':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_search_time_peanut = float(input("Enter minimum search time for peanuts (s): "))
        max_search_time_peanut = float(input("Enter maximum search time for peanuts (s): "))
        print("Search time ranges between {} and {} seconds".format(min_search_time_peanut, max_search_time_peanut))
        search_time_peanut = np.linspace(min_search_time_peanut, max_search_time_peanut, num=10)
        x_axis = search_time_peanut

    if nut_choice == 'h':
        min_search_time_hazel = float(input("Enter minimum search time for hazelnuts (s): "))
        max_search_time_hazel = float(input("Enter maximum search time for hazelnuts (s): "))
        print("Search time ranges between {} and {} seconds".format(min_search_time_hazel, max_search_time_hazel))
        search_time_hazel = np.linspace(min_search_time_hazel, max_search_time_hazel, num=10)
        x_axis = search_time_hazel


if var_choice == 'Handling time':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_handle_time_peanut = float(input("Enter minimum handling time for peanuts (s): "))
        max_handle_time_peanut = float(input("Enter maximum handling time for peanuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(min_handle_time_peanut, max_handle_time_peanut))
        handle_time_peanut = np.linspace(min_handle_time_peanut, max_handle_time_peanut, num=10)
        x_axis = handle_time_peanut

    if nut_choice == 'h':
        min_handle_time_hazel = float(input("Enter minimum handling time for hazelnuts (s): "))
        max_handle_time_hazel = float(input("Enter maximum handling time for hazelnuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(min_handle_time_hazel, max_handle_time_hazel))
        handle_time_hazel = np.linspace(min_handle_time_hazel, max_handle_time_hazel, num=10)
        x_axis = handle_time_hazel

if var_choice == 'Search energy':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_search_energy_peanut = float(input("Enter minimum energy used to search for peanuts (Kcal): "))
        max_search_energy_peanut = float(input("Enter maximum energy used to search for peanuts (Kcal): "))
        print("Search energy ranges between {} and {} calories".format(min_search_energy_peanut,
                                                                       max_search_energy_peanut))
        search_energy_peanut = np.linspace(min_search_energy_peanut, max_search_energy_peanut, num=10)
        x_axis = search_energy_peanut

    if nut_choice == 'h':
        min_search_energy_hazel = float(input("Enter minimum energy used to search for hazelnuts (Kcal): "))
        max_search_energy_hazel = float(input("Enter maximum energy used to search for hazelnuts (Kcal): "))
        print("Search energy ranges between {} and {} calories".format(min_search_energy_hazel,
                                                                       max_search_energy_hazel))
        search_energy_hazel = np.linspace(min_search_energy_hazel, max_search_energy_hazel, num=10)
        x_axis = search_energy_hazel

if var_choice == 'Handling energy':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_handle_energy_peanut = float(input("Enter minimum energy used to handle peanuts (Kcal): "))
        max_handle_energy_peanut = float(input("Enter maximum energy used to handle peanuts (Kcal): "))
        print("Handling energy ranges between {} and {} calories".format(min_handle_energy_peanut,
                                                                         max_handle_energy_peanut))
        handle_energy_peanut = np.linspace(min_handle_energy_peanut, max_handle_energy_peanut, num=10)
        x_axis = handle_energy_peanut

    if nut_choice == 'h':
        min_handle_energy_hazel = float(input("Enter minimum energy used to handle hazelnuts (Kcal): "))
        max_handle_energy_hazel = float(input("Enter maximum energy used to handle hazelnuts (Kcal): "))
        print("Handling energy ranges between {} and {} calories".format(min_handle_energy_hazel,
                                                                         max_handle_energy_hazel))
        handle_energy_hazel = np.linspace(min_handle_energy_hazel, max_handle_energy_hazel, num=10)
        x_axis = handle_energy_hazel

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
ax1.set_xlabel(var_choice)
ax1.set_ylabel('Net rate')

ax2.plot(x_axis, net_efficiency_hazel, label='Hazelnut')
ax2.plot(x_axis, net_efficiency_peanut, label='Peanut')
ax2.legend()
ax2.set_xlabel(var_choice)
ax2.set_ylabel('Net efficiency')

ax3.plot(x_axis, gross_rate_hazel, label='Hazelnut')
ax3.plot(x_axis, gross_rate_peanut, label='Peanut')
ax3.legend()
ax3.set_xlabel(var_choice)
ax3.set_ylabel('Gross rate')

ax4.plot(x_axis, gross_efficiency_hazel, label='Hazelnut')
ax4.plot(x_axis, gross_efficiency_peanut, label='Peanut')
ax4.legend()
ax4.set_xlabel(var_choice)
ax4.set_ylabel('Gross efficiency')
plt.show()


for i in range(len(x_axis) - 9):
    slope_1_net_rate = (net_rate_peanut[i + 1] - net_rate_peanut[i]) / (x_axis[i + 1] - x_axis[i])
    slope_2_net_rate = (net_rate_hazel[i + 1] - net_rate_hazel[i]) / (x_axis[i + 1] - x_axis[i])
    x_intersect_net_rate = (net_rate_hazel[i] - net_rate_peanut[i] + slope_1_net_rate * x_axis[i] - slope_2_net_rate *
                            x_axis[i]) / (slope_1_net_rate - slope_2_net_rate)
    print(f"The crossover point for net rate is: {x_intersect_net_rate:.2f}")

    slope_1_net_efficiency = (net_efficiency_peanut[i + 1] - net_efficiency_peanut[i]) / (x_axis[i + 1] - x_axis[i])
    slope_2_net_efficiency = (net_efficiency_hazel[i + 1] - net_efficiency_hazel[i]) / (x_axis[i + 1] - x_axis[i])
    x_intersect_net_efficiency = (net_efficiency_hazel[i] - net_efficiency_peanut[i] + slope_1_net_efficiency *
                                  x_axis[i] - slope_2_net_efficiency * x_axis[i]) / (slope_1_net_efficiency -
                                                                                     slope_2_net_efficiency)
    print(f"The crossover point for net efficiency is: {x_intersect_net_efficiency:.2f}")

    slope_1_gross_rate = (gross_rate_peanut[i + 1] - gross_rate_peanut[i]) / (x_axis[i + 1] - x_axis[i])
    slope_2_gross_rate = (gross_rate_hazel[i + 1] - gross_rate_hazel[i]) / (x_axis[i + 1] - x_axis[i])
    x_intersect_gross_rate = (gross_rate_hazel[i] - gross_rate_peanut[i] +
                              slope_1_gross_rate * x_axis[i] - slope_2_gross_rate * x_axis[i]) / (slope_1_gross_rate -
                                                                                                  slope_2_gross_rate)
    print(f"The crossover point for gross rate is: {x_intersect_gross_rate:.2f}")

    slope_1_gross_efficiency = (gross_efficiency_peanut[i + 1] - gross_efficiency_peanut[i]) / (x_axis[i + 1] -
                                                                                                x_axis[i])
    slope_2_gross_efficiency = (gross_efficiency_hazel[i + 1] - gross_efficiency_hazel[i]) / (x_axis[i + 1] - x_axis[i])
    x_intersect_gross_efficiency = (gross_efficiency_hazel[i] - gross_efficiency_peanut[i] + slope_1_gross_efficiency *
                                    x_axis[i] - slope_2_gross_efficiency * x_axis[i]) / (slope_1_gross_efficiency -
                                                                                         slope_2_gross_efficiency)
    print(f"The crossover point for gross efficiency is: {x_intersect_gross_efficiency:.2f}")


