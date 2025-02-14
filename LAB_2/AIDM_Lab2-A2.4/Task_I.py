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

print(data['calories']) 

transform = data.copy()

# subplots
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# Original histogram
ax[0, 0].hist(transform['calories'])
ax[0, 0].set_title('Calories frequency distribution')
ax[0, 0].set_xlabel('Calories')
ax[0, 0].set_ylabel('Frequency')
#ax[0, 0].set_yscale('log')

# Log1p transform
transform['log'] = transform['calories'].transform(np.log10)
ax[0, 1].hist(transform['log'])#, bins=30, density=True
ax[0, 1].set_title('Log10 of Calories Distribution')
ax[0, 1].set_xlabel('Log10Calories')
ax[0, 1].set_ylabel('Frequency')
#ax[0, 1].set_yscale('log')

# Cube transform, for cube root = np.power(x, 1/3)
transform['cube'] = transform['calories'].transform(lambda x: np.power(x, 3))
ax[1, 0].hist(transform['cube']) #, bins=30, density=True
ax[1, 0].set_title('Cube of Calories Distribution')
ax[1, 0].set_xlabel('Cube Calories')
ax[1, 0].set_ylabel('Frequency')


#Cube root transform
transform['cube_root'] = transform['calories'].transform(lambda x: np.power(x, 1/3))
ax[1, 1].hist(transform['cube_root']) #, bins=30, density=True
ax[1, 1].set_title('Cube root of Calories Distribution')
ax[1, 1].set_xlabel('Calories')
ax[1, 1].set_ylabel('Frequency')

# Save &/or display
plt.savefig('LAB_2/AIDM_Lab2-A2.4/Task-I_calories_transformations.png')
##plt.show()
