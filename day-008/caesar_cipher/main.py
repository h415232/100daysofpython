'''
Day: 8
Date: 30-July-2023
Name: Ceasar Cipher (FINAL)
'''
import art, os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_using = True

def caesar(text, shift, direction):
    # Set value of lenght of alphabet list
    alphabet_len = len(alphabet)

    # Correct the value of shift
    if shift % (alphabet_len) != 0:
        shift = shift % (alphabet_len)

    cipher = ""
    # Construct Cipher, will disregard char that not in alphabet list
    for val in text:
        if val not in alphabet:
            cipher += val
        else:
            cur_ind = alphabet.index(val)

            if direction.lower() in ("e", "encode"):
                new_ind = (cur_ind + shift) % alphabet_len

                if new_ind >= alphabet_len:
                    if shift == alphabet_len:
                        new_ind = cur_ind
                    else:
                        new_ind = shift - 1
            elif direction.lower() in ("d", "decode"):
                new_ind = (cur_ind - shift) % alphabet_len

                if new_ind < 0:
                    new_ind = alphabet_len - new_ind  

            cipher += alphabet[new_ind]

    return cipher  

######## MAIN ########
os.system('clear')
print(art.logo)

while is_using:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction.lower() not in ("e", "encode", "d", "decode"):
        print("Choice is invalid, exiting")
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print("Your caesar cipher msg is: " + caesar(text, shift, direction))

    state = input("Do you want to do another? (Y) or (N) ")

    if state.lower() not in ("y", "yes"):
        is_using = False
        print("Exiting")