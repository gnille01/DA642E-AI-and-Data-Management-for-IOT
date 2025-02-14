"""
I- 
    Based on the instruction on the distribution transformation, 
    transform the "calories" column to take the shape of a distribution close to normal distribution. 
    The current distribution looks something like the below figure. 
    Experiment with different transforms (log, cube, etc.) to find the right one. 
    Use a transform to make the data distribution more consistent, 
    meaning there are values on each column (1pts - Mandatory)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'LAB_2/AIDM_Lab2-A2.4/aw_fb_data.csv'

data = pd.read_csv(file_path, delimiter=',') 

print(data.head()) 

data['calories'].hist() #The function plots the distribution of the data in the "calories" column

plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.title('Calories frequency distribution')
plt.savefig('LAB_2/AIDM_Lab2-A2.4/calories_histogram.png') # Save the histogram 
## plt.show() # Display the plot

# transfrom the data
transform = data.copy()
# Log transform
transform['log'] = transform['calories'].transform(np.log10)
transform['log'].hist()

plt.title('Log10 of Calories Distribution')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.savefig('LAB_2/AIDM_Lab2-A2.4/calories_log_histogram.png') # Save the log plot
## plt.show() # Display the plot

# Cube transform
"""transform['cube'] = transform['calories'].transform(lambda x: np.power(x, 3))
transform['cube'].hist()"""

# Cube root transform, github copilot suggestion
transform['cube_root'] = transform['calories'].transform(lambda x: np.power(x, 1/3))
transform['cube_root'].hist()

plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.title('Cube Root of Calories Distribution')
plt.savefig('LAB_2/AIDM_Lab2-A2.4/calories_cube_histogram.png') # Save the cube plot
## plt.show() # Display the plot

