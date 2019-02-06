#These are the functions we can use to encrypt and decrypt the message
#when the subsituted value is known between the two people.

from sys import exit
from string import ascii_lowercase, ascii_uppercase


def Encrypter(message, substituteBy):
    """
    Parameters:
        message - A string that needs to be encrypted/decrypted
        substituteBy - An integer that tells the function how much
        the alphabets needs to be substituted by.
    
    Returns:
        The encrypted/decrypted message.
    """

    lowerAlpha = ascii_lowercase
    upperAlpha = ascii_uppercase

    encrypted = ""
    for i in message:

        if i in lowerAlpha:
            indexNum = lowerAlpha.index(i) + substituteBy
            encryptLetter = lowerAlpha[ (indexNum - len(lowerAlpha)) if (indexNum // len(lowerAlpha) == 1) else indexNum]
            encrypted += encryptLetter

        elif i in upperAlpha:
            indexNum = upperAlpha.index(i) + substituteBy
            encryptLetter = upperAlpha[ (indexNum - len(upperAlpha)) if (indexNum // len(upperAlpha) == 1) else indexNum]
            encrypted += encryptLetter

        else:
            encrypted += i


    return encrypted


if __name__ == '__main__':

    lowerAlpha = ascii_lowercase
    upperAlpha = ascii_uppercase

    usrCmd = input("Would you like to encrypt or decrypt your message? \n > ").lower()

    message = input("Enter the message that needs to be modified : \n > " )

    substituteBy = int(input("By what value would you like to substitute the alphabets ? \n > "))


    if "encrypt" in usrCmd :
        substituteBy += 1
        print(Encrypter(message, substituteBy))

    elif "decrypt" in usrCmd :
        substituteBy = - substituteBy - 1
        print(Encrypter(message, substituteBy))

    else:
        print("Computer couldn't understand your input. \n command not recognized.")
        exit(0)
