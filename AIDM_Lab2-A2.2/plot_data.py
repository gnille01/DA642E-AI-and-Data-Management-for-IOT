"""
I- Collect the data in a CSV file and submit it with the rest of your results (2pts-Mandatory)

II- Visualize the data with a line graph with two axes with criteria below (1pt-Mandatory)

    plot 6 axis of data
    Add labels for each axes (Acceleration (m.sq/s.sq), Time(seconds)),
    Turn on the grids 
    Add legend on the top right corner - the name of your plots should be Ax, Ay, Az, Gx, Gy, Gz

"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data/data.csv'
data = pd.read_csv(file_path, delimiter=',')

print(data)

fig, ax = plt.subplots()
ax.plot(data[' Ax'], data[' Ay'], data[' Az'])
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Accelerometer')
ax.grid(True)
ax.legend(['Accelerometer logging'])

"""ax.plot(data[' Gx'], data[' Gy'], data[' Gz'])
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Gyroscope')
ax.grid(True)
ax.legend(['Gyroscope logging'])"""


plt.savefig('data/plot_Acceleration.png')
plt.show()
plt.close()