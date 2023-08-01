# Day: 16
# Date: 01-Aug-2023
# Name: Coffee Maker OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instantiate all objects
coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Global variable
is_using = True


while is_using:
    option = input(f"What would you like ({coffee_menu.get_items()}): ").lower()
    
    order = coffee_menu.find_drink(option)

    if order and coffee_maker.is_resource_sufficient(order) \
            and money_machine.make_payment(order.cost):
        coffee_maker.make_coffee(order)
    elif option == "report":
        coffee_maker.report()
    elif option == "off":
        is_using = False