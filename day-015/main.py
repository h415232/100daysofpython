# Day: 15
# Date: 31-July-2023
# Name: Text-based Coffee Maker

from coffee_machine_data import MENU, resources


def show_report():
    ''' Helper function to show status of resources in the coffee machine '''
    for item in resources:
        if item == "money":
            resource_text = f"${resources[item]}"
        elif item in ("water", "milk"):
            resource_text = f"{resources[item]}ml"
        else:
            resource_text = f"{resources[item]}g"
        
        print(f"{item.title()}: {resource_text}")


def check_resources(drink):
    ''' Helper function to check if coffee maker can do the drink giver current resources'''
    resources_lacking = []
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] - MENU[drink]["ingredients"][ingredient] < 0:
            resources_lacking.append(ingredient)

    return resources_lacking


def get_money():
    ''' Calculate the coins put into the coffee maker '''
    q = int(input("How many 'Quarters'? "))
    d = int(input("How many 'Dimes'? "))
    n = int(input("How many 'Nickels?' "))
    p = int(input("How many 'Pennies?' "))

    return q*0.25 + d*0.10 + n*0.05 + p*0.01


def cost_coffee(drink):
    ''' Helper function to return the cost of drink '''
    return MENU[drink]["cost"]


def can_buy_coffee(money, drink):
    ''' Helper function to return if user can buy the coffee with the given coins'''
    return money - cost_coffee(drink) >= 0
                               

def calc_change(money, drink):
    ''' Helper function to calculate the change (if any) '''
    return money - cost_coffee(drink)


def update_resource(drink):
    ''' Helper function to update the resources after making the coffee '''
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

    resources["money"] += cost_coffee(drink)


def make_coffee(drink):
    ''' Function to facilitate coffee making '''
    lacking_resources = check_resources(drink)

    if not(lacking_resources): 
        money = get_money()

        print(f"You put ${money:0.2f} into the machine")
        if can_buy_coffee(money, drink):
            change = calc_change(money, drink)
            if change > 0:
                print(f"Here is ${change:0.2f} dollars in change")
            
            update_resource(drink)
            print(f"Here's your {drink}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded")
    else:
        for item in lacking_resources:
            print(f"Sorry there is not enough {item}")


def coffee_maker():
    ''' Function to mimic coffee maker '''
    is_using = True

    while is_using:
        option = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if option in ("espresso", "e"):
            make_coffee("espresso")
        elif option in ("latte", "l"):
            make_coffee("latte")
        elif option in ("cappuccino", "c"):
            make_coffee("cappuccino")
        elif option in ("report", "r"):
            show_report()
        elif option in ("off"):
            is_using = False


# Trigger Coffee Maker
coffee_maker()