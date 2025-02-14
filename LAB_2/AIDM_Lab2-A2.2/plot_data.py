"""
I- Collect the data in a CSV file and submit it with the rest of your results (2pts-Mandatory)

II- Visualize the data with a line graph with two axes with criteria below (1pt-Mandatory)

    plot 6 axis of data
    Add labels for each axes (Acceleration (m.sq/s.sq), Time(seconds)),
    Turn on the grids 
    Add legend on the top right corner - the name of your plots should be Ax, Ay, Az, Gx, Gy, Gz

II- (Manipulate the data) With one of the the functions mentioned in the instruction above, 
    write a code which deletes rows of data from your dataset that the acceleration is 0 or close to 0. 
    This will compress your signals to look something like the right graphs below in Fig. 9. 
    Visualize the data again with the above criteria in a line graph. 
    Pay attention that you need to look at the data and define the threshold accordingly for deleting stationary data. 
    The threshold might be different for different axes  (2pt-Mandatory)
"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data/data.csv'
data = pd.read_csv(file_path, delimiter=',')
print(data)

# Remove trailing spaces in column names
data.columns = data.columns.str.strip()

# filter out rows where Ax, Ay, or Az are between 0.5 and -0.5
data = data[((data['Ax'] > 0.2) | (data['Ax'] < -0.2)) & ((data['Ay'] > 0.2) | (data['Ay'] < -0.2)) & ((data['Az'] > 0.2) | (data['Az'] < -0.2))
            & ((data['Gx'] > 20) | (data['Gx'] < -20)) & ((data['Gy'] > 20) | (data['Gy'] < -20)) & ((data['Gz'] > 20) | (data['Gz'] < -20))]
print(data)

# Convert the 'Time' column to datetime
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S')
# Calculate elapsed time in seconds
data['Elapsed Time'] = (data['Time'] - data['Time'].iloc[0]).dt.total_seconds()

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# First Y-axis (Left): Accelerometer Data
ax1.plot(data['Elapsed Time'], data['Ax'], label='Ax', color='b')
ax1.plot(data['Elapsed Time'], data['Ay'], label='Ay', color='g')
ax1.plot(data['Elapsed Time'], data['Az'], label='Az', color='r')
ax1.set_xlabel('Time Elapsed (seconds)')
ax1.set_ylabel('Acceleration (m/s²)', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(True)

# Create a second Y-axis (Right) for Gyroscope Data
ax2 = ax1.twinx()
ax2.plot(data['Elapsed Time'], data['Gx'], label='Gx', linestyle='dashed', color='c')
ax2.plot(data['Elapsed Time'], data['Gy'], label='Gy', linestyle='dashed', color='m')
ax2.plot(data['Elapsed Time'], data['Gz'], label='Gz', linestyle='dashed', color='y')
ax2.set_ylabel('Gyroscope (°/s)', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Combine legends for both axes
fig.legend(loc='upper right', bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

plt.savefig('data/plot_Acc-Gyr-Plot.png')
plt.show()
