import string

lowercase = string.ascii_lowercase
def substitute(word, substituteBy):
    lWord = word.lower()
    encrypted = ""
    for i in lWord:
        if i in lowercase:
            encryptLetter = lowercase[lowercase.index(i) + substituteBy]
            encrypted += encryptLetter
        else:
            encrypted += i
    return encrypted

print(substitute("I like fries", 2))
# returns "k nkmg htkgu"
          
