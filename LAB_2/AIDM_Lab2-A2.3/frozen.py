"""
I- Visualize the indoor and outdoor temperature in one plot with different colors of your choice for the last week (strat from the top 02-12-2018 to 08-12-2018). (2 pts-Mandatory)

II- Do these modifications on the dataframe made from the CSV dataset: (3pts Mandatory)

    Change the "In" and "Out" text of the "Out\In" column to 1 and 0 respectively.
    Separate the date and time in the "noted_date" column, into two separate columns.
    Keep only the data of the last day 08-12-2018, and remove the rest of the rows with the appropriate function

"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = "AIDM_Lab2-A2.3/IOT-temp.csv" ## AIDM_Lab2-A2.3\IOT-temp.csv
data = pd.read_csv(file_path, delimiter=",")

# Convert date column
data['noted_date'] = pd.to_datetime(data['noted_date'], format='%d-%m-%Y %H:%M')

# Filter data for the last week (02-12-2018 to 08-12-2018)
start_date = "2018-12-02"
end_date = "2018-12-08"
filtered_data = data[(data['noted_date'] >= start_date) & (data['noted_date'] <= end_date)]
print(filtered_data)

# Separate "In" and "Out" temperature data
data_in = filtered_data[filtered_data["out/in"] == "In"]
data_out = filtered_data[filtered_data["out/in"] == "Out"]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(data_in['noted_date'], data_in["temp"], label="Indoor Temperature", color="blue")
ax.plot(data_out['noted_date'], data_out["temp"], label="Outdoor Temperature", color="red")

ax.set_xlabel("Date")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Indoor vs Outdoor Temperature (02-Dec-2018 to 08-Dec-2018)")

ax.grid(True)

ax.legend(loc="upper right")

plt.xticks(rotation=45)

plt.savefig("AIDM_Lab2-A2.3/temperature_last_week.png")
plt.show()
