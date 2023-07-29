'''
Day: 8
Date: 30-July-2023
Name: Ceasar Cipher Decryption (PART 3)
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO - combine encrypt and decrypt into 1 function called caesar(), with 3 param: text, shift, direction

def caesar(text, shift, direction):
    # Set value of lenght of alphabet list
    alphabet_len = len(alphabet)

    # Correct the value of shift
    if shift % (alphabet_len) != 0:
        shift = shift % (alphabet_len)

    cipher = ""
    # Construct Cipher
    for val in text:
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
            
        else:
            print("Selection invalid, exiting")
            break   

        cipher += alphabet[new_ind]

    return cipher

print("Your caesar cipher msg is: " + caesar(text, shift, direction))     