'''
Day: 9
Date: 30-July-2023
Name: Silent Bidding
'''

import os, art 

# Global Variables
bidders = {}
is_using = True

while is_using:
    os.system('clear')
    print(art.logo)
    print("Welcome to the secret auction program.")
    
    bidder_name = input("What is your name?: ")
    bidder_bid = int(input("What's your bid?: $"))

    bidders[bidder_name] = bidder_bid

    state = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if state.lower() not in ("y", "yes"):
        is_using = False
    
    os.system('clear')

print("The winner is " + max(bidders) + " with a bid of $" + str(max(bidders.values())))