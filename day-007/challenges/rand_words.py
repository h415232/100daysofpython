'''
Day: 7
Date: 29-July-2023
Name: [Challenge 1] Random word picking
'''

#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list) 

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

if guess in chosen_word:
    print('Y')
else:
    print('N')

print(chosen_word)