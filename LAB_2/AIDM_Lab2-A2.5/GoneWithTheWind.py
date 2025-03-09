# Task A2.4: Gone with the Wind! (3pt - Optional)
"""

"""

# libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
filepath = 'LAB_2/AIDM_Lab2-A2.5/data/Climate2016.csv'

# clean data
with open(filepath, 'r') as f:
    lines = f.readlines()

clean_header = lines[0].replace('""', '').strip('"').strip()
lines[0] = clean_header + '\n'

with open('LAB_2/AIDM_Lab2-A2.5/data/cleaned_file.csv', 'w') as f:
    f.writelines(lines)

# pd dataframe
data = pd.read_csv('LAB_2/AIDM_Lab2-A2.5/data/cleaned_file.csv')
data = data.rename(columns={'winddeg (deg)"':'winddeg (deg)'}) 

print(data.head())

df = data.copy()
velocity = df['windvelo (m/s)']
direction = df['winddeg (deg)']

# directon to radian: radians(90 - (wind direction))
df['radian'] = np.radians(90 - df['winddeg (deg)'])

# Compute wind vector components
df['Wind X (m/s)'] = velocity * np.cos(df['radian'])
df['Wind Y (m/s)'] = velocity * np.sin(df['radian'])

# Normalize
df['Wind X (m/s)'] = (df['Wind X (m/s)'] - df['Wind X (m/s)'].min()) / (df['Wind X (m/s)'].max() - df['Wind X (m/s)'].min())
df['Wind Y (m/s)'] = (df['Wind Y (m/s)'] - df['Wind Y (m/s)'].min()) / (df['Wind Y (m/s)'].max() - df['Wind Y (m/s)'].min())

df.to_csv("LAB_2/AIDM_Lab2-A2.5/data/Climate2016_transformed.csv", index=False)

# Visualize
plt.figure(figsize=(10, 5))

plt.subplot(1,2,1)
plt.hist2d(direction,velocity, bins=(50,50), vmax=400)
plt.xlabel("Wind Direction (deg)")
plt.ylabel("Wind Velocity (m/s)")
plt.title("Before Transformation")

plt.subplot(1,2,2)
plt.hist2d(df['Wind X (m/s)'], df['Wind Y (m/s)'], bins=(50,50), vmax=400)
plt.xlabel("Wind X (m/s)")
plt.ylabel("Wind Y (m/s)")
plt.title("After Transformation")

plt.savefig("LAB_2/AIDM_Lab2-A2.5/data/wind_plot.png")
plt.show()
