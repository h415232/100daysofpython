# Day: 24
# Date: 17-Aug-2023
# Name: Mail Merge Challenge

# CONSTANTS
INVITED_NAMES_DIR = "Input/Names/invited_names.txt"
START_LETTER_DIR = "Input/Letters/starting_letter.txt"
OUTPUT_LETTER_DIR = "Output/ReadyToSend/"
OUTPUT_LETTER_NAMESPACE = "letter_for_"
OUTPUT_LETTER_FILETYPE = ".txt"
NAME_PLACEHOLDER = "[name]"

# Get the names of the invited people
with open(file=INVITED_NAMES_DIR, mode="r") as f:
    names = f.readlines()

# Clean the data to remove "\n" on extracted names
for i in range(len(names)):
    names[i] = names[i].replace("\n","")

# Get the letter template
with open(file=START_LETTER_DIR, mode="r") as f:
    letter_template = f.read()

# Generate the letters
for name in names:
    out_letter_file = OUTPUT_LETTER_DIR + OUTPUT_LETTER_NAMESPACE + name + OUTPUT_LETTER_FILETYPE

    with open(file=out_letter_file, mode="w") as f:
        f.write(letter_template.replace(NAME_PLACEHOLDER, name))