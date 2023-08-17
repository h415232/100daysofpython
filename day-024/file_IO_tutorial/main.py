# Tutorial on file I/O

# Traditional way of opening a file

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()


# Another way of opening file

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

    # No need to put file.close() as after the "with"
    #   python will automatically close the file for you :)

# Writing to a file
#with open("my_file.txt", mode="w") as file:
#    file.write("New Text") # This will automatically automatically remove all, and put this instead

# This will append to the last line, use '\n' to start on new line
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text")