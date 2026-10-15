import pandas as pd # in case of error, install pnadas using: pip install pandas
# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')
new_data = {
'Temp': 366,
'Humd': 901,
'Label': 0
}
df = df._append(new_data, ignore_index=True)
# Step 3: Save the DataFrame to a new CSV file
df.to_csv("data.csv", index=False)

# Run this multiple times with different fake values to inject invalid data.
# Collect at least 1000 data points in data.csv for Part 2

# Label 1 = valid data, Label 0 = invalid data
