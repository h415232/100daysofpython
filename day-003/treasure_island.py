'''
Day: 3
Date: 28-July-2023
Name: Treasure Island
'''

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

option = input("Do you want to go left (L) or right (R)? ")
if option.lower() in ("l", "left"):
    option = input("You entered into a cave, you see a body of water that seems to lead to the treasure. Do you want to (Swim) or (Wait) till dawn?" )
    if option.lower() == "wait":
        option = input("You patiently waited till the night and you saw a magical doors dawn upon you. Which door do you enter, Red (R), Blue (B), or Yellow (Y)? ")
        if option.lower in ("b", "blue"):
            print("You choose the blue door, and as you enter the blue door, you saw a majestic sight OF A BEAST! You tried to run but it is too late. YOU ARE DEAD!")
        elif option.lower in ("r", "red"):
            print("You choose the red door, and unfortunately it led you towards death. YOU ARE DEAD!")
        else:
            print("You choose the yellow door. The door led you to a peaceful path, and you saw the treasure! YOU WON!")
    else:
        print("While swimming to the horizon, you are attacked by a trout! YOU ARE DEAD!")
else:
    print("You fall into a hole, YOU ARE DEAD!")