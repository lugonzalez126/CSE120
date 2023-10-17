import pandas as pd 

file_path = "Test1.xlsx"

sheet_name = "in"

columns_to_read = ["time", "chrg"]

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Filter the DataFrame to include only the specified columns
selected_columns = df[columns_to_read]

# Print the selected columns

for index, row in selected_columns.iterrows():
    time_data = row['time']
    chrg_data = row['chrg']
    

print(selected_columns)