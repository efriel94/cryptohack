# Import colorama for colorful text.
from colorama import Fore, init

init()


# function for caesar cipher encryption
def caesar_cipher(message: str, key: int, decrypt: bool = False) -> str:
    # store result
    result = ''

    # implement encryption or decryption
    for index in message:
        if index.isalpha():
            shift = key if not decrypt else -key
            if index.islower():
                result += chr(((ord(index) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(index) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += index
    
    return result


def crack_caesar_cipher(mesg: str):

    # loop through all possible keys
    for i in range(26):
        decrypted_data = caesar_cipher(mesg,i,decrypt=False)
        print(f"Key {i}: {decrypted_data}")




message = "Hello World"
ciphertext = "Byffi Qilfx"
cryptohack_ciphertext = "HDSKLAU LJAH ZAVVWF VQFSEAU"
key = 20

ciphertext = caesar_cipher(message, key, decrypt=False)
print(ciphertext)
crack_caesar_cipher(cryptohack_ciphertext)


#     # for every index in msg
#         # check if its alphabetical 
#             # check if uppercase
#                 # perform shift
#             # check if lowercase
#                 # perform shift
#         # stays as is
    
#     # return result
    



# # Define a function for Caesar cipher encryption.
# def implement_caesar_cipher(text, key, decrypt=False):
#     # Initialize an empty string to store the result.
#     result = ""

#     # Iterate through each character in the input text.
#     for char in text:
#         # Check if the character is alphabetical.
#         if char.isalpha():
#             # Determine the shift value using the provided key (or its negation for decryption).
#             shift = key if not decrypt else -key

#             # Check if the character is lowercase
#             if char.islower():
#                 # Apply the Caesar cipher encryption/decryption formula for lowercase letters.
#                 result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
#             else:
#                 # Apply the Caesar cipher encryption/decryption formula for uppercase letters.
#                 result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
#         else:
#             # If the character is not alphabetical, keep it as is e.g. numbers, punctuation
#             result += char
#     # Return the result, which is the encrypted or decrypted text
#     return result


# # Define a function for cracking the Caesar cipher.
# def crack_caesar_cipher(ciphertext):
#     # Iterate through all possible keys (0 to 25) as there 26 alphabets.
#     for key in range(26):
#         # Call the caesar_cipher function with the current key to decrypt the text.
#         decrypted_text = implement_caesar_cipher(ciphertext, key, decrypt=True)

#         # Print the result, showing the decrypted text for each key
#         print(f"{Fore.RED}Key {key}: {decrypted_text}")


# # Initiate a continuous loop so the program keeps running.
# while True:
#     # Accept user input.
#     encrypted_text = input(f"{Fore.GREEN}[?] Please Enter the text/message to decrypt: ")
#     # Check if user does not specify anything.
#     if not encrypted_text:
#         print(f"{Fore.RED}[-] Please specify the text to decrypt.")
#     else:
#         crack_caesar_cipher(encrypted_text)

