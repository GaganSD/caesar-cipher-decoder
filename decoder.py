
import string
import matplotlib.pyplot as plt

alphabets = string.ascii_lowercase + string.ascii_uppercase

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

D = count_value(open("encrypted-files/aesop-fabels.txt", 'r'))

plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.xlabel('alphabets')
plt.ylabel('Times the char repeated')
plt.legend()
plt.show()
