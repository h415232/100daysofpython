# Day 30
# Date: 22-Aug-2023
# Name: NATO Alphabet [IMPROVED]

import pandas as pd

FILE_DB = "nato_phonetic_alphabet.csv"

is_using = True

# Import the csv file and generate a dataframe
df = pd.read_csv(FILE_DB)

# From dataframe, construct a dictionary for letter as key and word as val
nato_alpha = {v.letter: v.code for k,v in df.iterrows()}

def convert_to_nato(str):
    str_list = [i.upper() for i in str]
    nato_val = [nato_alpha[i] for i in str_list]

    return nato_val

def print_nato(nato):    
    str_list = [i.upper() for i in str]
    for i in range(len(str_list)):
        print(f"{str_list[i]} for {nato[i]}")
    

# MAIN PROGRAM
while is_using:
    try:
        str = input("Enter the string to convert to NATO Alphabet: ")
        nato = convert_to_nato(str)
    except KeyError:
        print("Sorry, only letters are supported")
    else:
        is_using = False


print_nato(nato)