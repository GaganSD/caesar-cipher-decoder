import string

lowercase = string.ascii_lowercase
def cipherEncrypt(word, substituteBy):
    lWord = word.lower()
    encrypted = ""
    for i in lWord:
        if i in lowercase:
            encryptLetter = lowercase[lowercase.index(i) + substituteBy]
            encrypted += encryptLetter
        else:
            encrypted += i
    return encrypted

def cipherDecrypt(message, subsitutedValue):
    decrypted = ""

    for i in message:
    
        if i in lowercase:
            decryptedLetter = lowercase[lowercase.index(i) - subsitutedValue]
            decrypted += decryptedLetter
        else:
            decrypted += i
    
    return decrypted
    
    
print(cipherEncrypt("I like fries", 2))
# returns "k nkmg htkgu"

print(cipherDecrypt("k nkmg htkgu", 2))
# returns "i like fries"