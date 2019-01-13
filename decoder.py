
import string

alphabets = string.ascii_lowercase + string.ascii_uppercase

a = """
THE BOASTING TRAVELLER


A Man once went abroad on his travels, and when he came home he
had wonderful tales to tell of the things he had done in foreign
countries. Among other things, he said he had taken part in a
jumping-match at Rhodes, and had done a wonderful jump which no one
could beat. "Just go to Rhodes and ask them," he said; "every one will
tell you it's true." But one of those who were listening said, "If you
can jump as well as all that, we needn't go to Rhodes to prove it.
Let's just imagine this is Rhodes for a minute: and now--jump!"

    Deeds, not words.
"""

def count_value(text_file):
    lower_text = text_file.lower()
    hist = {}
    for i in lower_text:
        if i in alphabets:
            if i not in hist:
                hist[i] = 1
            else:
                hist[i] += 1
    return hist
print(count_value(a))

lowerAlpha = string.ascii_lowercase
upperAlpha = string.ascii_uppercase

def cipherEncrypt(message, substituteBy):
    encrypted = ""
    for i in message:

        if i in lowerAlpha:
            encryptLetter = lowerAlpha[lowerAlpha.index(i) + substituteBy]
            encrypted += encryptLetter
        elif i in upperAlpha:
            encryptLetter = upperAlpha[upperAlpha.index(i) + substituteBy]
            encrypted += encryptLetter
        else:
            encrypted += i

    return encrypted

b = cipherEncrypt(a, 2)

print(count_value(a))
