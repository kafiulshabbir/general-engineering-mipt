import numpy as np
import matplotlib.pyplot as plt

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
data_array = data_array * int_to_volt
#2 - time to seconds
x_axis = np.linspace(0, time_operation, data_array.size)

#4-Colour, shape, size of line, and markers
#4-Frequencies of showinf markers and legends
#5-min and max values for the axes
#6- axis lalels
#7-The plots name with a set location and automatic continual to a new line in case of long name
#8-main and additional grid, with colour and style set up
#9-text with time of charging and discharging
#10-commit and push to reprository
fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)
ax.plot(x_axis, data_array)
fig.savefig("test.svg")
plt.show()