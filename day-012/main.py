# Day: 12
# Date: 30-July-2023
# Name: Number Guessing Game

# Pseudocode

# 1. Randomize number between 1 and 100
# 2. Ask user if difficulty is easy (give 10 attemps) or hard (give 5 attemps)
# 3. Ask user to guess, and keep track of how many guesses
# 4. If user guess correctly, win 
# 5. If user did not guess correctly, guess again till attemps are not exhausted
# 6. If attemp is exhausted, user lose

from art import logo
import os, random

attempt = 0
is_win = False
comp_number = random.randint(1,100)

os.system("clear")
print(logo)
print("Welcom to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
choice = input("Choose the difficulty, Type 'easy' or 'hard': ")

if choice.lower() in ("easy", "e"):
    attempt = 10
elif choice.lower() in ("hard", "h"):
    attempt = 5

while attempt != 0 and not(is_win):
    print(f"You have {attempt} attemp(s) remaining to guess the number.")
    num_guess = int(input("Make a guess: "))

    if num_guess == comp_number:
        is_win = True
    elif num_guess > comp_number:
        print("Too high!\nGuess Again.")
    else:
        print("Too low!\nGuess Again.")

    attempt -= 1

if attempt == 0:
    print(f"You've run out of guesses! The answer was {comp_number}! You lose.")
elif attempt > 0 and is_win:
    print(f"You got it! The answer was {comp_number}.")