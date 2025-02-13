import pandas as pd

file_path = "AIDM_Lab2-A2.3/IOT-temp.csv"
data = pd.read_csv(file_path, delimiter=",")

# Convert date column
data['noted_date'] = pd.to_datetime(data['noted_date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Print unique dates to verify format
print(data['noted_date'].dt.date.unique())

# Separate noted_date into date and time columns
data['date'] = data['noted_date'].dt.date
data['time'] = data['noted_date'].dt.time

# Ensure the target date exists in the dataset
if pd.to_datetime('2018-12-08').date() in data['date'].values:
    # Keep only the data for the last day (08-12-2018)
    data = data[data['date'] == pd.to_datetime('2018-12-08').date()]
    print('Dtaa for 08-12-2018 found!')
else:
    print("No data found for 08-12-2018")

# Change "In" → 1 and "Out" → 0 in the 'out/in' column
data['out/in'] = data['out/in'].replace({'In': 1, 'Out': 0})

# Drop the original 'noted_date' column
data.drop(columns=['noted_date'], inplace=True)

data.to_csv("AIDM_Lab2-A2.3/modified_data.csv", index=False)

print(data.head())
