letters = 'abcdefghijklmnopqrstuvwxyz'

msgLen = len(letters)

def encrypt(plainText, key):

    cipherText = " "

    for letter in plainText:

        letter = letter.lower()

        if not letter == '':

            index = letters.find(letter)

            if index == -1:

                cipherText += letter

            else:

                new_index = index + key

                if new_index >= msgLen:

                    new_index -= msgLen

                cipherText += letters[new_index]

    return cipherText





def decrypt(cipherText, key):

    plainText = " "

    for letter in cipherText:

        letter = letter.lower()

        if not letter == '':

            index = letters.find(letter)

            if index == -1:

                plainText += letter

            else:

                new_index = index - key

                if new_index < 0:

                    new_index += msgLen

                plainText += letters[new_index]

    return plainText





print(" do you want to encrypt or decrypt :")

user_input = input('e/d: ').lower()

print()

if user_input == 'e':

    print("encrypt mode")

    print()

    key = int(input('enter the key'))

    text = input('enter the text to encrypt:')

    cipherText = encrypt(text, key)

    print(f"the cipherText is : {cipherText}")

else :

    print("decrypt mode")

    print()

    key = int(input('enter the key'))

    text = input('enter the message to decrypt:')

    plainText = decrypt(text, key)

    print(f"the plaintext is : {plainText}")
