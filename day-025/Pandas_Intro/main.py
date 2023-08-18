# Data Reading

FILE_DIR = "weather_data.csv"
NEW_FILE = "new_data.csv"

# Traditional
# data = []
# with open(FILE_DIR, "r") as f:
#     data = f.readlines()

# print(data)

# Working with CSV

# import csv

# with open(FILE_DIR, "r") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(data)
# print(temperatures)


'''
PANDAS:
DataFrame - Table, group of Series
Series - Vector, aka. Single Column
'''

import pandas as pd

data = pd.read_csv(FILE_DIR)
print(type(data)) # Pandas DataFrame
print(data)
print(type(data["temp"])) # Pandas Series
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(data["temp"].mean())

# Getting information by row
print(data[data.day == "Monday"])

# Equivalent code from above
print(data[data["day"] == "Monday"])

# Priting the row with the highest Temp
print(data[data.temp == data.temp.max()])

# Data filtering
monday = data[data.day == "Monday"]
print(monday.condition)

temp = monday.temp
temp_in_f = (temp*.18) + 32
print(temp)
print(temp_in_f)


# Creating DataFrame from dictionary
dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pd.DataFrame(dict)
print(new_data)

# Transferring Pandas DataFrame into a CSV
new_data.to_csv(NEW_FILE)