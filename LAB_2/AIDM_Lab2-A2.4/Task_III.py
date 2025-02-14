"""
III- 
    Visualize "steps", "heart_rate", and "calories" 
    of the first three participants in three plots with subplots (stacked plot), 
    in a way that the steps of each three participants are depicted with different colored lines, 
    the same for other two datasets. 
    The legends should be on the top corner of each plot 
    (participant #1, participant #2, participant#3) (2pts - Mandatory)
"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'LAB_2/AIDM_Lab2-A2.4/Task-II_aw_fb_data.csv'

data = pd.read_csv(file_path, delimiter=',')

# copy the data
df = data.copy()

# Create subplots: 3 rows, 1 column
fig, ax = plt.subplots(2, 2, figsize=(10, 12))

# Stackplot for Steps
ax[0, 0].stackplot(df.index, df['steps'], labels=['Steps'], colors=['blue'])
ax[0, 0].set_title('Steps of participants')
ax[0, 0].set_ylabel('Steps')
ax[0, 0].set_xlabel('Participant')
ax[0, 0].legend()

# Stackplot for Heart Rate
ax[1, 0].stackplot(df.index, df['hear_rate'], labels=['Heart Rate'], colors=['green'])
ax[1 ,0].set_title('Heart Rate of participants')
ax[1 ,0].set_ylabel('Heart Rate ')
ax[1, 0].set_xlabel('Participant')
ax[1 ,0].legend()

# Stackplot for Calorie
ax[0, 1].stackplot(df.index, df['calories'], labels=['Calories'], colors=['red'])
ax[0, 1].set_title('Calories of participants')
ax[0,1].set_ylabel('Calories ')
ax[0,1].set_xlabel('Participant')
ax[0,1].legend()

# Stackplot for Steps, Heart Rate, Calories
ax[1,1].stackplot(df.index, df['steps'], df['hear_rate'], df['calories'], labels=['Steps', 'Heart Rate', 'Calories'])
ax[1,1].set_title('Steps, Heart Rate, Calories of participants')
ax[1,1].set_ylabel('Steps, Heart Rate, Calories')
ax[1,1].set_xlabel('Participant')
ax[1,1].legend()


# Adjust layout & Show
plt.tight_layout()
plt.savefig('LAB_2/AIDM_Lab2-A2.4/Task-III_steps_heart_rate_calories.png')

plt.show()
