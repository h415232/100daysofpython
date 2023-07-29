'''
Day: 8
Date: 30-July-2023
Name: Ceasar Cipher Decryption (PART 2)
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):

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
    
    return encrypt_msg

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"

    '''
    1. Loop within the string to decrypt
    2. Check the index of the letter in the "alphabet"
    3. Construct by shifting the letter by alphabet[index - shift]
    '''

    # Set value of lenght of alphabet list
    alphabet_len = len(alphabet)

    # Correct the value of shift [To avoid dealing with shift value that is greater than 26]
    if shift % (alphabet_len) != 0:
        shift = shift % (alphabet_len)

    decrypt_msg = ""

    # Construct decryption message
    for val in text:
        cur_ind = alphabet.index(val)
        new_ind = (cur_ind - shift) % alphabet_len

        if new_ind < 0:
            new_ind = alphabet_len - new_ind

        decrypt_msg += alphabet[new_ind]
    
    return decrypt_msg

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction.lower() in ("e", "encode"):
    print("Encrypted msg: " + encrypt(text, shift))
elif direction.lower() in ("d", "decode"):
    print("Decrypted msg: " +decrypt(text, shift))
else:
    print("Selection invalid, exiting")        