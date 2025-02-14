"""
V- 
    Split the dataset into three categories with the following distribution: 
    Train (70%), Validation (15%), and Test (15%) (1pts - Mandatory)
"""

import pandas as pd

file_path = 'LAB_2/AIDM_Lab2-A2.4/Task_IV_aw_fb_data.csv'

data = pd.read_csv(file_path, delimiter=',')

df = data.copy()

# Split the dataset
train = df.sample(frac=0.7, random_state=0)
df.drop(train.index, inplace=True)

validation = df.sample(frac=0.5, random_state=0)
test = df.drop(validation.index)

print("Train: ", train.shape)
print("Validation: ", validation.shape)
print("Test: ", test.shape)

print(train)
print(validation)
print(test)


# train.to_csv('LAB_2/AIDM_Lab2-A2.4/Task_V_train.csv', index=False)
# validation.to_csv('LAB_2/AIDM_Lab2-A2.4/Task_V_validation.csv', index=False)
# test.to_csv('LAB_2/AIDM_Lab2-A2.4/Task_V_test.csv', index=False)
