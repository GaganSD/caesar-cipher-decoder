import string

alphabets = string.ascii_lowercase
upperAlpha = string.ascii_uppercase
def cipherEncrypt(message, substituteBy):
    encrypted = ""
    for i in message:
        if i in alphabets:
            encryptLetter = alphabets[alphabets.index(i) + substituteBy]
            encrypted += encryptLetter
        elif i in upperAlpha:
            encryptLetter = upperAlpha[upperAlpha.index(i) + substituteBy]
            encrypted += encryptLetter
        else:
            encrypted += i
    return encrypted

def cipherDecrypt(message, subsitutedValue):
    decrypted = ""

    for i in message:
    
        if i in alphabets:
            decryptedLetter = alphabets[alphabets.index(i) - subsitutedValue]
            decrypted += decryptedLetter
        elif i in upperAlpha:
            decryptedLetter = upperAlpha[upperAlpha.index(i) - subsitutedValue]
            decrypted += decryptedLetter
        else:
            decrypted += i
    
    return decrypted


print(cipherEncrypt("I like fries", 2))
# returns "k nkmg htkgu"

print(cipherDecrypt("K nkmg htkgu", 2))
# returns "I like fries"