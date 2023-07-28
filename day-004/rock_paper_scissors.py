'''
Day: 4
Date: 28-July-2023
Name: Simple Rock-Paper-Scissors
'''

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)    
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper, '2' for Scissors. \n"))

print("You chose: \n" + options[player_choice])

comp_choice = random.randint(0,len(options)-1)
print("Computer chose: \n" + options[comp_choice])

result = player_choice - comp_choice

if player_choice == 0:
    if result == 0:
        result_output = "Draw"
    elif result == -1:
        result_output = "Lose"
    else:
        result_output = "Win"
elif player_choice == 1:
    if result == 1:
        result_output = "Win"
    elif result == 0: 
        result_output = "Draw"
    else:
        result_output = "Lose"
else:
    if result == 2:
        result_output = "Lose"
    elif result == 1:
        result_output = "Win"
    else:
        result_output = "Draw"

print("Result: " + result_output)

'''
0,1,2

0 - 0 = 0  --draw
0 - 1 = -1 --lose
0 - 2 = -2 --win

1 - 0 = 1  --win
1 - 1 = 0  --draw
1 - 2 = -1 --lose

2 - 0 = 2  --lose
2 - 1 = 1  --win
2 - 2 = 0  --draw
'''


