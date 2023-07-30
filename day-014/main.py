# Day: 14
# Date: 30-July-2023
# Name: Higher Lower Game

from game_data import data
import art, random, os

# Pseudocode
# 1. Initially, randomly choose 2 items in the list
# 2. Ensure that 2 items are not the same
# 3. Print out Compare A to B
# 4. Ask user which is higher
# 5. If choice >= than compare, score += 1
# 6. Whaterver the choice, it becomes A, and randomly choose B, replay game
# 7. If choice < compare, show score and game over

def show_logo():
    os.system("clear")
    print(art.logo)

def show_vs():
    print(art.vs)

def show_info(info,state):
    if state == 1:
        print(f"Compare A: {info['name']}, {info['description']}, from {info['country']}")
    else:
        print(f"Against B: {info['name']}, {info['description']}, from {info['country']}")

def show_score(score):
    show_logo()
    print(f"You're right! Current score: {score}")

def show_lose(score):
    show_logo()
    print(f"Sorry, that's wrong. Final score: {score}")

def pick_data():
    return random.choice(data)

def is_same(a, b):
    if a == b:
        return True
    else:
        return False

def unique_data(a):
    b = pick_data()

    while is_same(a,b):
        b = pick_data()

    return b    

def bigger_follower(a,b):
    if a['follower_count'] > b['follower_count']:
        return a
    else:
        return b

def is_correct(a, b, choice):
    if choice == 'a':
        if a["follower_count"] >= b["follower_count"]:
            return True
        else:
            return False
    if choice == 'b':
        if b["follower_count"] >= a["follower_count"]:
            return True
        else:
            return False

def higher_lower():
    # Initialize
    score = 0
    is_playing = True

    # Pick data for comparison
    a = pick_data()
    b = unique_data(a)

    # Show UI
    show_logo()

    while is_playing:
        show_info(a,1)
        show_vs()
        show_info(b,2)

        choice = input("Who has more followers? Type 'A' or 'B': ")

        if is_correct(a,b,choice.lower()):
            score += 1
            a = bigger_follower(a,b)
            b = unique_data(a)
            
            show_score(score)
        else:
            show_lose(score)
            is_playing = False

# Call the main game
higher_lower()