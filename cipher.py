#These are the functions we can use to encrypt and decrypt the message
#when the subsituted value is known between the two people.

from sys import exit
from string import ascii_lowercase, ascii_uppercase
import operator


# Uses dictionaries to 
ops = {
    "+": operator.add,
    "-": operator.sub
}


usrCmd = input("Do you want the code to be encrypted or decrypted ? \n")
usrCmd.lower()

if "encrypt" in usrCmd :
    sign = "+"
elif "decrypt" in usrCmd :
    sign = "-"
else:
    print("Computer couldn't understand your input. \n Try again and please enter a valid input.")
    exit(0)


ops_func = ops[sign]


message = input("Enter the message that needs to be modified : \n" )
substituteBy = int(input("By what value would you like to substitute the alphabets ? \n"))

lowerAlpha = ascii_lowercase
upperAlpha = ascii_uppercase

def cipher(message, substituteBy):
    """
    Parameters:
        message - A string that needs to be encrypted/decrypted
        substituteBy - An integer that tells the function how much
        the alphabets needs to be substituted by.
    
    Returns:
        The encrypted/decrypted message.
    """
    encrypted = ""
    for i in message:

        if i in lowerAlpha:
            indexNum = lowerAlpha.index(i) + ops_func(substituteBy, 1)
            encryptLetter = lowerAlpha[ (indexNum - len(lowerAlpha)) if (indexNum // len(lowerAlpha) == 1) else indexNum]
            encrypted += encryptLetter

        elif i in upperAlpha:
            indexNum = upperAlpha.index(i) + ops_func(substituteBy, 1)
            encryptLetter = upperAlpha[ (indexNum- len(upperAlpha)) if (indexNum // len(upperAlpha) == 1) else indexNum]
            encrypted += encryptLetter

        else:
            encrypted += i

    return encrypted


print( cipher(message, substituteBy) )


# print(cipher("L olnh iulhv", 2))
# returns "I like fries"
