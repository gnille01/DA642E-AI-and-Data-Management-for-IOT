"""
II- Visualize the data with a line graph with two axes: time & temperature with criteria below (1pt-Mandatory)

    The color of the line should be orange
    Add labels for each axes (Temperature (degrees Celsius), Time(seconds)),
    Turn on the grids 
    Add legend on the top right corner - temperature

"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data/data.csv'
data = pd.read_csv(file_path, delimiter=',')

print(data)

fig, ax = plt.subplots()
ax.plot(data['Timesteps'], data[' Temperature'], color='orange')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Temperature (degrees Celsius)')
ax.grid(True)
ax.legend(['Temperature'], loc='upper right')

plt.savefig('data/plot_temp.png')
plt.show()
plt.close()