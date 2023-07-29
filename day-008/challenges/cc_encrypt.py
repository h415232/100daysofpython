'''
Day: 8
Date: 30-July-2023
Name: Ceasar Cipher Encryption (PART 1)
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    '''
    1. Loop within the string to encrypt
    2. Check the index of the letter in the "alphabet"
    3. Shift should be recalculated, if shift%len(alphabet) != 0, then shift = shift%len(alphabet)
    4. Construct an encrypt_string by setting the new string as alphabet_index + shift
    5. if alphabet_index + shift % len != 0, new string will be alphabet[modulo]
    '''
    # Set value of lenght of alphabet list
    alphabet_len = len(alphabet)

    # Correct the value of shift
    if shift % (alphabet_len) != 0:
        shift = shift % (alphabet_len)
    
    # Construct the new text (encryption)
    encrypt_msg = ''
    for val in text:
        cur_ind = alphabet.index(val)
        new_ind = (cur_ind + shift) % alphabet_len

        if new_ind >= alphabet_len:
            if shift == alphabet_len:
                new_ind = cur_ind
            else:
                new_ind = shift - 1

        encrypt_msg += alphabet[new_ind]
    
    return print(f"The encoded text is {encrypt_msg}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text,shift)