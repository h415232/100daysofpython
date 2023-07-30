# Day: 10
# Date: 30-July-2023
# Name: Calculator (Text-based)

from art import logo
import os

# Global Variable
operations = ['+', '-', '*', '/']
is_using = True
is_continue = True

def calc(a, b, opr):
    if opr == "+":
        return a + b
    elif opr == "-":
        return a - b
    elif opr == "*":
        return a * b
    elif opr == "/":
        return a / b

while is_using:
    os.system("clear")
    print(logo)
    a = float(input("What's the first number?: "))

    is_continue = True
    while is_continue:
        for operation in operations:
            print(operation)
        opr = ""
        while opr not in operations:
            opr = input("Pick an operation: ")

            if opr not in operations:
                print(f"Operation {opr} not supported!")

        b = float(input("What's the next number?: "))
        res = calc(a,b,opr)
        print(f"{a} {opr} {b} = {res}")

        continue_calc = input(f"Type 'y' to continue calculating with {a}, type 'n' to start a new calculation, type 'x' to exit calculator: ")

        if continue_calc.lower() in ("x", "exit"):
            is_continue = False
            is_using = False
        elif continue_calc.lower() not in ("y", "y"):
            is_continue = False
        else:
            a = res