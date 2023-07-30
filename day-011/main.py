# Day: 11
# Date: 30-July-2023
# Name: Blackjack (Text-based)

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


# Pseudocode
#  1. Ask if user wants to play blackjack, if yes, play blackjack, else, close program
#  2. User will be initially given 2 cards from cards
#  3. Computer will be initially given 2 cards from cards
#  4. Computer will show the first card from hand
#  5. Ask if user will get more card. User can get more card for as long as the sum of card is < 21
#  6. Computer will get more card for as long as the hand card sum is < 17
#  7. Check if user card > 21, if yes, user lose
#  8. Check if computer card is > 21, if yes and user_card <= 21, user win
#  9. If user_card == computer_card, draw 
# 10. If user_card > computer_card, win
# 11. Go back to step 1

from art import logo
import os, random

# Global Variable
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sum_of_card(cards_at_hand):
    ''' Obtains the sum of card at hand, taking note of Ace which can be interpreted as either 1 or 11 '''
    tot = sum(cards_at_hand)
    if cards[0] in cards_at_hand and tot > 21:
        tot -= 10
    
    return tot

def draw_card(cards_at_hand):
    ''' Will draw 1 card from the list "cards" '''
    cards_at_hand.append(random.choice(cards))

    return cards_at_hand

def show_user_card_info(cards_at_hand):
    ''' Will give the current state of user cards '''
    print(f"   Your cards: {cards_at_hand}, current score: {sum_of_card(cards_at_hand)}")

def show_comp_card_info(cards_at_hand):
    ''' Will give the current state of computer cards '''
    print(f"   Computer's first card: {cards_at_hand[0]}")

def show_game_info(user,comp):
    show_user_card_info(user)
    show_comp_card_info(comp)

def is_bust(cards_at_hand):
    if sum_of_card(cards_at_hand) > 21:
        return True
    else: 
        return False

def is_comp_hitting(comp_cards):
    ''' Check if Computer should still hit '''
    if sum_of_card(comp_cards) < 17:
        return True
    else:
        return False

def show_final_card_info(user, comp, stat):
    ''' Shows the final info of the game'''
    print(f"   Your final hand: {user}, final score: {sum_of_card(user)}")
    print(f"   Computer's final hand: {comp}, final score: {sum_of_card(comp)}")
    
    if stat == "win":
        print("You win!")
    elif stat == "lose":
        print("You lose!")
    else:
        print("It's a draw!")

def check_who_won(user, comp):
    ''' Logic of checking who won the game'''
    tot_user = sum_of_card(user)
    tot_comp = sum_of_card(comp)

    if is_bust(user):
        show_final_card_info(user, comp, "lose")
    elif is_bust(comp):
        show_final_card_info(user, comp, "win")
    elif tot_user == tot_comp:
        show_final_card_info(user, comp, "draw")
    elif tot_user > tot_comp:
        show_final_card_info(user, comp, "win")
    elif tot_user < tot_comp:
        show_final_card_info(user, comp, "lose")
    

def blackjack():
    ''' Implementation of simplified BlackJack game '''
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if choice.lower() in ("yes", "y"):
        os.system("clear")
        print(logo)

        # Initialize 
        is_user_hitting = True
        user_cards = []
        comp_cards = []

        # Draw initial cards (2 cards) for user and comp
        for i in range(2):
            draw_card(user_cards)
            draw_card(comp_cards)

        # Hit (get card) if possible for user
        while not(is_bust(user_cards)) and is_user_hitting:
            show_game_info(user_cards, comp_cards)
            choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if choice.lower() not in ("yes", "y"):
                is_user_hitting = False
                break

            # Draw 1 card
            draw_card(user_cards)

        # Computer hits
        while not(is_bust(comp_cards)) and is_comp_hitting(comp_cards):
            draw_card(comp_cards)

        # Check who won
        check_who_won(user_cards, comp_cards)

        # Reset the game to go back to start
        blackjack()

# Initialize the game
blackjack()