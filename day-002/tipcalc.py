'''
 Day: 2
Date: 27-July-2023
Name: Tip Calculator
'''

print('Welcome to the tip calculator')

tot_bill = float(input('What is the total bill? '))
tot_pers = float(input('How many people to split the bill? '))
tip_perc = float(input('How many percentage tip would you like to give? 10, 12, or 15? '))

tip = (tot_bill + tot_bill * (tip_perc/100)) / tot_pers

print(f'Each person should pay: {tip:0.2f}')