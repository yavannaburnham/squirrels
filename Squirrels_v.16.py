import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


# Set baseline values
gain_peanut = np.linspace(3, 3, num=50)
gain_hazel = np.linspace(7, 7, num=50)
search_time_peanut = np.linspace(1, 1, num=50)
search_time_hazel = np.linspace(4, 4, num=50)
handle_time_peanut = np.linspace(2, 2, num=50)
handle_time_hazel = np.linspace(1, 1, num=50)
search_energy_peanut = search_time_peanut
search_energy_hazel = search_time_hazel
handle_energy_peanut = handle_time_peanut
handle_energy_hazel = handle_time_hazel
x_axis = gain_peanut
var_label = "Energy gain"


# Define currencies
def currencies(gain, search_energy, handle_energy, search_time, handle_time):
    net_rate = (gain - search_energy - handle_energy) / (search_time + handle_time)
    net_efficiency = (gain - search_energy - handle_energy) / (search_energy + handle_energy)
    gross_rate = (gain / (search_time + handle_time))
    gross_efficiency = (gain / (search_energy + handle_energy))
    return [net_rate, net_efficiency, gross_rate, gross_efficiency]


var_choice_1 = input("First variable: enter '1' for energy gain, '2' for search time, or "
                     "'3' for handling time: ")
if var_choice_1 == '1':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_gain_peanut = float(input("Enter minimum energy gain for peanuts: "))
        max_gain_peanut = float(input("Enter maximum energy gain for peanuts: "))
        print("Kcal gained ranges between {} and {}".format(min_gain_peanut, max_gain_peanut))
        gain_peanut = np.linspace(min_gain_peanut, max_gain_peanut, num=50)
        x_axis = gain_peanut
        var_label = "Energy gain"

    if nut_choice == 'h':
        min_gain_hazel = float(input("Enter minimum energy gain for hazelnuts (Kcal): "))
        max_gain_hazel = float(input("Enter maximum energy gain for hazelnuts (Kcal): "))
        print("Energy gained ranges between {} and {} calories".format(min_gain_hazel, max_gain_hazel))
        gain_hazel = np.linspace(min_gain_hazel, max_gain_hazel, num=50)
        x_axis = gain_hazel
        var_label = "Energy gain"


if var_choice_1 == '2':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_search_time_peanut = float(input("Enter minimum search time for peanuts (s): "))
        max_search_time_peanut = float(input("Enter maximum search time for peanuts (s): "))
        print("Search time ranges between {} and {} seconds".format(min_search_time_peanut, max_search_time_peanut))
        search_time_peanut = np.linspace(min_search_time_peanut, max_search_time_peanut, num=50)
        x_axis = search_time_peanut
        var_label = "Search time"

    if nut_choice == 'h':
        min_search_time_hazel = float(input("Enter minimum search time for hazelnuts (s): "))
        max_search_time_hazel = float(input("Enter maximum search time for hazelnuts (s): "))
        print("Search time ranges between {} and {} seconds".format(min_search_time_hazel, max_search_time_hazel))
        search_time_hazel = np.linspace(min_search_time_hazel, max_search_time_hazel, num=50)
        x_axis = search_time_hazel
        var_label = "Search time"


if var_choice_1 == '3':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_handle_time_peanut = float(input("Enter minimum handling time for peanuts (s): "))
        max_handle_time_peanut = float(input("Enter maximum handling time for peanuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(min_handle_time_peanut, max_handle_time_peanut))
        handle_time_peanut = np.linspace(min_handle_time_peanut, max_handle_time_peanut, num=50)
        x_axis = handle_time_peanut
        var_label = "Handling time"

    if nut_choice == 'h':
        min_handle_time_hazel = float(input("Enter minimum handling time for hazelnuts (s): "))
        max_handle_time_hazel = float(input("Enter maximum handling time for hazelnuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(min_handle_time_hazel, max_handle_time_hazel))
        handle_time_hazel = np.linspace(min_handle_time_hazel, max_handle_time_hazel, num=50)
        x_axis = handle_time_hazel
        var_label = "Handling time"

search_energy_peanut = search_time_peanut
search_energy_hazel = search_time_hazel
handle_energy_peanut = handle_time_peanut
handle_energy_hazel = handle_time_hazel

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

# Create an empty list to store results of comparison
result_net_rate = []

# Iterate over each value in both net rates and compare them using a loop
for i in range(len(x_axis)):
    if net_rate_hazel[i] > net_rate_peanut[i]:
        result_net_rate.append(1)
    else:
        result_net_rate.append(0)

# Find index in 'result' where 0 becomes 1 or vice versa
cross_net_rate = None
for i in range(len(result_net_rate)):      # for every value in result:
    if result_net_rate[i] != result_net_rate[i-1]:  # if i is not the same value
        # as i - 1 then this is the cross-over point
        cross_net_rate = i

# Scale the cross-over point to the chosen variable
if cross_net_rate is not None:
    print(f"The cross-over point for net rate is at: {x_axis[cross_net_rate]:.1f}")
else:
    print("No cross-over point for net rate found.")


result_net_efficiency = []
for i in range(len(x_axis)):
    if net_efficiency_hazel[i] > net_efficiency_peanut[i]:
        result_net_efficiency.append(1)
    else:
        result_net_efficiency.append(0)

cross_net_efficiency = None
for i in range(len(result_net_efficiency)):
    if result_net_efficiency[i] != result_net_efficiency[i-1]:
        cross_net_efficiency = i

if cross_net_efficiency is not None:
    print(f"The cross-over point for net efficiency is at: {x_axis[cross_net_efficiency]:.1f}")
else:
    print("No cross-over point for net efficiency found.")

result_gross_rate = []
for i in range(len(x_axis)):
    if gross_rate_hazel[i] > gross_rate_peanut[i]:
        result_gross_rate.append(1)
    else:
        result_gross_rate.append(0)

cross_gross_rate = None
for i in range(len(result_gross_rate)):
    if result_gross_rate[i] != result_gross_rate[i-1]:
        cross_gross_rate = i

if cross_gross_rate is not None:
    print(f"The cross-over point for gross rate is at: {x_axis[cross_gross_rate]:.1f}")
else:
    print("No cross-over point for gross rate found.")

result_gross_efficiency = []
for i in range(len(x_axis)):
    if gross_efficiency_hazel[i] > gross_efficiency_peanut[i]:
        result_gross_efficiency.append(1)
    else:
        result_gross_efficiency.append(0)

cross_gross_efficiency = None
for i in range(len(result_gross_efficiency)):
    if result_gross_efficiency[i] != result_gross_efficiency[i-1]:
        cross_gross_efficiency = i

if cross_gross_efficiency is not None:
    print(f"The cross-over point for gross efficiency is at: {x_axis[cross_gross_efficiency]:.1f}")
else:
    print("No cross-over point for gross efficiency found.")

# Plot currencies
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Currency Comparison')
ax1.plot(x_axis, net_rate_hazel, label='Hazelnut')
ax1.plot(x_axis, net_rate_peanut, label='Peanut')
ax1.legend()
ax1.set_xlabel(var_label)
ax1.set_ylabel('Net rate')
ax1.set_xticks(x_axis)
ax1.xaxis.set_major_locator(plt.MaxNLocator(11))
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax2.plot(x_axis, net_efficiency_hazel, label='Hazelnut')
ax2.plot(x_axis, net_efficiency_peanut, label='Peanut')
ax2.legend()
ax2.set_xlabel(var_label)
ax2.set_ylabel('Net efficiency')
ax2.set_xticks(x_axis)
ax2.xaxis.set_major_locator(plt.MaxNLocator(11))
ax2.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))


ax3.plot(x_axis, gross_rate_hazel, label='Hazelnut')
ax3.plot(x_axis, gross_rate_peanut, label='Peanut')
ax3.legend()
ax3.set_xlabel(var_label)
ax3.set_ylabel('Gross rate')
ax3.set_xticks(x_axis)
ax3.xaxis.set_major_locator(plt.MaxNLocator(11))
ax3.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))


ax4.plot(x_axis, gross_efficiency_hazel, label='Hazelnut')
ax4.plot(x_axis, gross_efficiency_peanut, label='Peanut')
ax4.legend()
ax4.set_xlabel(var_label)
ax4.set_ylabel('Gross efficiency')
ax4.set_xticks(x_axis)
ax4.xaxis.set_major_locator(plt.MaxNLocator(11))
ax4.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.show(block=False)

var_choice_2 = input("Second variable: enter '1' for energy gain, '2' for search time, "
                     "'3' for handling time: ")
if var_choice_2 == '1':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_gain_peanut = float(input("Enter minimum energy gain for peanuts: "))
        max_gain_peanut = float(input("Enter maximum energy gain for peanuts: "))
        print("Kcal gained ranges between {} and {}".format(min_gain_peanut, max_gain_peanut))
        gain_peanut = np.linspace(min_gain_peanut, max_gain_peanut, num=50)

    if nut_choice == 'h':
        min_gain_hazel = float(input("Enter minimum energy gain for hazelnuts (Kcal): "))
        max_gain_hazel = float(input("Enter maximum energy gain for hazelnuts (Kcal): "))
        print("Energy gained ranges between {} and {} calories".format(min_gain_hazel, max_gain_hazel))
        gain_hazel = np.linspace(min_gain_hazel, max_gain_hazel, num=50)

if var_choice_2 == '2':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_search_time_peanut = float(input("Enter minimum search time for peanuts (s): "))
        max_search_time_peanut = float(input("Enter maximum search time for peanuts (s): "))
        print("Search time ranges between {} and {} seconds".format(min_search_time_peanut, max_search_time_peanut))
        search_time_peanut = np.linspace(min_search_time_peanut, max_search_time_peanut, num=50)

    if nut_choice == 'h':
        min_search_time_hazel = float(input("Enter minimum search time for hazelnuts (s): "))
        max_search_time_hazel = float(input("Enter maximum search time for hazelnuts (s): "))
        print("Search time ranges between {} and {} seconds".format(min_search_time_hazel, max_search_time_hazel))
        search_time_hazel = np.linspace(min_search_time_hazel, max_search_time_hazel, num=50)

if var_choice_2 == '3':
    nut_choice = input("Enter 'p' for peanut or 'h' for hazelnut: ")

    if nut_choice == 'p':
        min_handle_time_peanut = float(input("Enter minimum handling time for peanuts (s): "))
        max_handle_time_peanut = float(input("Enter maximum handling time for peanuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(min_handle_time_peanut, max_handle_time_peanut))
        handle_time_peanut = np.linspace(min_handle_time_peanut, max_handle_time_peanut, num=50)

    if nut_choice == 'h':
        min_handle_time_hazel = float(input("Enter minimum handling time for hazelnuts (s): "))
        max_handle_time_hazel = float(input("Enter maximum handling time for hazelnuts (s): "))
        print("Handling time ranges between {} and {} seconds".format(min_handle_time_hazel, max_handle_time_hazel))
        handle_time_hazel = np.linspace(min_handle_time_hazel, max_handle_time_hazel, num=50)

search_energy_peanut = search_time_peanut
search_energy_hazel = search_time_hazel
handle_energy_peanut = handle_time_peanut
handle_energy_hazel = handle_time_hazel

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

# Create an empty list to store results of comparison
result_net_rate = []

# Iterate over each value in both net rates and compare them using a loop
for i in range(len(x_axis)):
    if net_rate_hazel[i] > net_rate_peanut[i]:
        result_net_rate.append(1)
    else:
        result_net_rate.append(0)

# Find index in 'result' where 0 becomes 1 or vice versa
cross_net_rate = None
for i in range(len(result_net_rate)):      # for every value in result:
    if result_net_rate[i] != result_net_rate[i-1]:  # if i is not the same value
        # as i - 1 then this is the cross-over point
        cross_net_rate = i

# Scale the cross-over point to the chosen variable
if cross_net_rate is not None:
    print(f"The cross-over point for net rate is now at: {x_axis[cross_net_rate]:.1f}")
else:
    print("No cross-over point for net rate found.")


result_net_efficiency = []
for i in range(len(x_axis)):
    if net_efficiency_hazel[i] > net_efficiency_peanut[i]:
        result_net_efficiency.append(1)
    else:
        result_net_efficiency.append(0)

cross_net_efficiency = None
for i in range(len(result_net_efficiency)):
    if result_net_efficiency[i] != result_net_efficiency[i-1]:
        cross_net_efficiency = i

if cross_net_efficiency is not None:
    print(f"The cross-over point for net efficiency is now at: {x_axis[cross_net_efficiency]:.1f}")
else:
    print("No cross-over point for net efficiency found.")

result_gross_rate = []
for i in range(len(x_axis)):
    if gross_rate_hazel[i] > gross_rate_peanut[i]:
        result_gross_rate.append(1)
    else:
        result_gross_rate.append(0)

cross_gross_rate = None
for i in range(len(result_gross_rate)):
    if result_gross_rate[i] != result_gross_rate[i-1]:
        cross_gross_rate = i

if cross_gross_rate is not None:
    print(f"The cross-over point for gross rate is now at: {x_axis[cross_gross_rate]:.1f}")
else:
    print("No cross-over point for gross rate found.")

result_gross_efficiency = []
for i in range(len(x_axis)):
    if gross_efficiency_hazel[i] > gross_efficiency_peanut[i]:
        result_gross_efficiency.append(1)
    else:
        result_gross_efficiency.append(0)

cross_gross_efficiency = None
for i in range(len(result_gross_efficiency)):
    if result_gross_efficiency[i] != result_gross_efficiency[i-1]:
        cross_gross_efficiency = i

if cross_gross_efficiency is not None:
    print(f"The cross-over point for gross efficiency is now at: {x_axis[cross_gross_efficiency]:.1f}")
else:
    print("No cross-over point for gross efficiency found.")

# Plot currencies
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Currency Comparison')
ax1.plot(x_axis, net_rate_hazel, label='Hazelnut')
ax1.plot(x_axis, net_rate_peanut, label='Peanut')
ax1.legend()
ax1.set_xlabel(var_label)
ax1.set_ylabel('Net rate')
ax1.set_xticks(x_axis)
ax1.xaxis.set_major_locator(plt.MaxNLocator(11))
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax2.plot(x_axis, net_efficiency_hazel, label='Hazelnut')
ax2.plot(x_axis, net_efficiency_peanut, label='Peanut')
ax2.legend()
ax2.set_xlabel(var_label)
ax2.set_ylabel('Net efficiency')
ax2.set_xticks(x_axis)
ax2.xaxis.set_major_locator(plt.MaxNLocator(11))
ax2.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))


ax3.plot(x_axis, gross_rate_hazel, label='Hazelnut')
ax3.plot(x_axis, gross_rate_peanut, label='Peanut')
ax3.legend()
ax3.set_xlabel(var_label)
ax3.set_ylabel('Gross rate')
ax3.set_xticks(x_axis)
ax3.xaxis.set_major_locator(plt.MaxNLocator(11))
ax3.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))


ax4.plot(x_axis, gross_efficiency_hazel, label='Hazelnut')
ax4.plot(x_axis, gross_efficiency_peanut, label='Peanut')
ax4.legend()
ax4.set_xlabel(var_label)
ax4.set_ylabel('Gross efficiency')
ax4.set_xticks(x_axis)
ax4.xaxis.set_major_locator(plt.MaxNLocator(11))
ax4.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.show()
