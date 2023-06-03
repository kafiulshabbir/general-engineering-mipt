import numpy as np
import matplotlib.pyplot as plt

#time operation and volt will be changed later
time_operation = 1
int_to_volt = 1

#1 - importing and reading
with open("settings.txt", "r") as settings:
    #print(settings.read().split("\n"))
    tmp = [float(i) for i in settings.read().split("\n")]
    int_to_volt = tmp[0]
    time_operation = tmp[1]

#1 - importing and reading
data_array = np.loadtxt("data.txt", dtype=float)

#2 - decimals to volts
y_axis = data_array * int_to_volt

#2 - time to seconds
x_axis = np.linspace(0, time_operation, data_array.size)

fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)
#4-[done] Colour, shape, size of line, and markers
#4-[done]Frequencies of showinf markers and legends
ax.plot(x_axis, y_axis, label = "v(t)", color = 'blue', linewidth=1, marker = "o", markevery = 25, markersize = 10, markerfacecolor = 'red')

#6- axis lalels [done]
ax.set_xlabel("Time since start of charging[s]")
ax.set_ylabel("Potential difference across the capacitor, volts [V]")

#7-[done]The plots name with a set location and automatic continual to a new line in case of long name
ax.set_title("Graph of exponential dependence of Charging and Discharging of a capacitor in RC circuit", clip_on = False, loc = 'center')
ax.legend()

#5-[done]min and max values for the axes
x_min = x_axis.min()
x_max = 1.05*x_axis.max()
y_min = y_axis.min()
y_max  = 1.05*y_axis.max()

plt.xlim(left = x_min)
plt.xlim(right = x_max)
plt.ylim(bottom = y_min)
plt.ylim(top = y_max)

#8-main and additional grid, with colour and style set up
ax.set_xticks(np.arange(0, x_max, 10))
ax.set_xticks(np.arange(0, x_max, 2), minor = True)

ax.set_yticks(np.arange(0, y_max, 0.5))
ax.set_yticks(np.arange(0, y_max, 0.1), minor = True)

plt.grid(axis = 'x', which = 'major', color = 'black', linestyle = '-', visible = True)
plt.grid(axis = 'x', which = 'minor', color = 'grey', linestyle = '--', visible = True)
plt.grid(axis = 'y', which = 'major', color = 'black', linestyle = '-', visible = True)
plt.grid(axis = 'y', which = 'minor', color = 'grey', linestyle = '--', visible = True)
#9-text with time of charging and discharging
loc_downfall = 0
for i in range(len(y_axis) - 10):
    count = 0
    for j in range(4):
        if y_axis[i + j + 1] < y_axis[i + j]:
            count += 1
    if count == 4:
        loc_downfall = i
        break

time_start_dis = loc_downfall * time_operation / data_array.size

time_dis = time_operation - time_start_dis
#print(time_start_dis)
ax.text(70,2.8, "Time of charging = {:.1f}s\n\nTime of discharging = {:.2f}s".format(time_start_dis, time_dis))

fig.savefig("test.svg")
#plt.show()

#10-[DONE] commit and push to reprository