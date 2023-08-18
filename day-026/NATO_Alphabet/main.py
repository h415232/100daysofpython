# Day 26
# Date: 18-Aug-2023
# Name: NATO Alphabet

import pandas as pd

FILE_DB = "nato_phonetic_alphabet.csv"

# Import the csv file and generate a dataframe
df = pd.read_csv(FILE_DB)

# From dataframe, construct a dictionary for letter as key and word as val
nato_alpha = {v.letter: v.code for k,v in df.iterrows()}

def convert_to_nato(str):
    str_list = [i.upper() for i in str]
    nato_conv = [[(k,v) for k,v in nato_alpha.items() if i == k] for i in str_list]
    #nato_val = [nato_alpha[i] for i in str_list]

    return nato_conv

def print_nato(nato):    
    for i in range(len(nato)):
       if nato[i] != []:
           print(f"{nato[i][0][0]} for {nato[i][0][1]}")
       else:
           print()
    # str_list = [i.upper() for i in str]
    # for i in range(len(str_list)):
    #     print(f"{str_list[i]} for {nato[i]}")


# MAIN PROGRAM
str = input("Enter the string to convert to NATO Alphabet: ")
nato = convert_to_nato(str)
print_nato(nato)