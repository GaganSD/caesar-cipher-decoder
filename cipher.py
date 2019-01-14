#These are the functions we can use to encrypt and decrypt the message
#when the subsituted value is known between the two people.

import string
lowerAlpha = string.ascii_lowercase
upperAlpha = string.ascii_uppercase

def cipherEncrypt(message, substituteBy):
    encrypted = ""
    for i in message:

        if i in lowerAlpha:
            indexNum = lowerAlpha.index(i) + substituteBy + 1
            encryptLetter = lowerAlpha[ (indexNum - len(lowerAlpha)) if (indexNum // len(lowerAlpha) == 1) else indexNum]
            encrypted += encryptLetter

        elif i in upperAlpha:
            indexNum = upperAlpha.index(i) + substituteBy + 1
            encryptLetter = upperAlpha[ (indexNum- len(upperAlpha)) if (indexNum // len(upperAlpha) == 1) else indexNum]
            encrypted += encryptLetter

        else:
            encrypted += i

    return encrypted

def cipherDecrypt(message, subsitutedValue):
    decrypted = ""

    for i in message:

        if i in lowerAlpha:
            indexNum = lowerAlpha.index(i) - subsitutedValue - 1
            decryptedLetter = lowerAlpha[ (indexNum- len(lowerAlpha)) if (indexNum // len(lowerAlpha) == 1) else indexNum]
            decrypted += decryptedLetter

        elif i in upperAlpha:
            indexNum = upperAlpha.index(i) - subsitutedValue - 1
            decryptedLetter = upperAlpha[ (indexNum- len(upperAlpha)) if (indexNum // len(upperAlpha) == 1) else indexNum]
            decrypted += decryptedLetter

        else:
            decrypted += i

    return decrypted


# print(cipherDecrypt("L olnh iulhv", 2))
# returns "I like fries"

