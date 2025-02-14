"""
IV- 
    Normalize the "age", "height", and "weight", 
    and Standardize "steps" and "heart rate" columns 
    in a separate column at the end of the dataframe (1pts - Mandatory)
"""

import pandas as pd
import numpy as np

file_path = 'LAB_2/AIDM_Lab2-A2.4/Task-II_aw_fb_data.csv'

data = pd.read_csv(file_path, delimiter=',')

df = data.copy()

# Normalize the "age", "height", and "weight"
df['age_norm'] = (df['age'] - df['age'].min()) / (df['age'].max() - df['age'].min())
df['height_norm'] = (df['height'] - df['height'].min()) / (df['height'].max() - df['height'].min())
df['weight_norm'] = (df['weight'] - df['weight'].min()) / (df['weight'].max() - df['weight'].min())

# Standardize "steps" and "heart rate" columns
df['steps_std'] = (df['steps'] - df['steps'].mean()) / df['steps'].std()
df['heart_rate_std'] = (df['hear_rate'] - df['hear_rate'].mean()) / df['hear_rate'].std()

print(df.head())
print(df.tail())
df.to_csv('LAB_2/AIDM_Lab2-A2.4/Task_IV_aw_fb_data.csv', index=False)