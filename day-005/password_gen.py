'''
Day: 5
Date: 29-July-2023
Name: Simple Password Generator [Needs optimization]
'''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass_len = nr_letters + nr_symbols + nr_numbers
pass_content = [letters, numbers, symbols]
pass_content_len = [nr_letters, nr_numbers, nr_symbols]
password = ""

'''
1. Iterate for password lenght
2. For every iteration of password val, we will choose randomly if letters, numbers, or sym
3. After choosing pass_content, check if nr_x > 0, if nr_x > 0, nr_x -= 1
4. Randomly choose from the list 
5. If nr_x <= 0, randomize again 
'''

for i in range(0, pass_len+1):
    flag = True
    while flag:
        pass_content_choice = random.randint(0,2)

        if pass_content_len[pass_content_choice] > 0:
            pass_content_len[pass_content_choice] -= 1
            flag = False
        
        if sum(pass_content_len) == 0:
            flag = False

    password = password + random.choice(pass_content[pass_content_choice])

print(f"Your password is: {password}")