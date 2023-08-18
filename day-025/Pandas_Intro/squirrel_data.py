# Get a subset of data frame that will consolidate the
#  count of fur color counts
#  output the result in CSV file

import pandas as pd

FILE = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
FILE_RES = "squirrel_count.csv"

# Importing data from CSV
df = pd.read_csv(FILE)
print(df)

print(df["Primary Fur Color"])

color_count = df.groupby("Primary Fur Color").size()

print(color_count)
color_count.to_csv(FILE_RES)