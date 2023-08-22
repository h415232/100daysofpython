# File not found
#with open("a_file.txt") as file:
#    file.read()

# Key Error 
# Index Error
# Type Error

# try -> something that might cause an exeption
# execpt -> will go here if something failed
# else -> will go here if NOTHING FAILED
# finally -> will go here w/ or w/o failure in try block

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as err_msg:
#     print(f"The key {err_msg} does not exist.")    
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File closed")

#IndexError

h = float(input("Height: "))
w = int(input("Weight: "))


if h > 3:
    raise ValueError("Human Height should NOT be greater than 3 m")

bmi = w / (h**2)

print(bmi)