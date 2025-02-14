"""
II- 
    As mentioned before, the data reflects 49 participants. 
    Make a copy of the original dataframe and Find a way to keep one sample from each participant.  
    Therefore, the new dataframe should have 49 rows. 
    You should use a specific function or a mix of functions in the instruction. 
    Afterward, visualize the "age", "height", 
    and "weight" of the participants on each subplot (stacked plot). 
    Grids should be on, Legends should be on top, 
    and The color of the line plot for each subplot should be different. (2pts - Optional)
"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'LAB_2/AIDM_Lab2-A2.4/aw_fb_data.csv'

data = pd.read_csv(file_path, delimiter=',')

df = data.copy()

# drop duplicates of the same participant based on age, gender, height
df.drop_duplicates(subset=('age','gender','height'), keep='first', inplace=True)
df.reset_index(drop=True, inplace=True)
print("Row, Col: ", df.shape)
print(df.head())
print(df.tail())

df.to_csv('LAB_2/AIDM_Lab2-A2.4/Task-II_aw_fb_data.csv', index=False)

# Create subplots: 3 rows, 1 column
fig, ax = plt.subplots(2, 2, figsize=(10, 12))

# Stackplot for Age
ax[0, 0].stackplot(df.index, df['age'], labels=['Age'], colors=['blue'])
ax[0, 0].set_title('Age of participants')
ax[0, 0].set_ylabel('Age')
ax[0, 0].set_xlabel('Participant')
ax[0, 0].legend()

# Stackplot for Height
ax[1, 0].stackplot(df.index, df['height'], labels=['Height'], colors=['green'])
ax[1, 0].set_title('Height of participants')
ax[1, 0].set_ylabel('Height ')
ax[1, 0].set_xlabel('Participant')
ax[1, 0].legend()

# Stackplot for Weight
ax[0, 1].stackplot(df.index, df['weight'], labels=['Weight'], colors=['red'])
ax[0, 1].set_title('Weight of participants')
ax[0, 1].set_ylabel('Weight ')
ax[0, 1].set_xlabel('Participant')
ax[0, 1].legend()

# Stackplot for Age, Height, Weight
ax[1, 1].stackplot(df.index, df['age'], df['height'], df['weight'], 
                   colors=['blue', 'green', 'red'] ,labels=['Age', 'Height', 'Weight'])
ax[1, 1].set_title('Age, Height, Weight of participants')
ax[1, 1].set_ylabel('Age, Height, Weight')
ax[1, 1].set_xlabel('Participant')
ax[1, 1].legend()

# Adjust layout & Show
plt.tight_layout()
plt.savefig('LAB_2/AIDM_Lab2-A2.4/Task-II_age_height_weight.png')
plt.show()

