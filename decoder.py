from cipher import Encrypter
from string import ascii_lowercase, ascii_uppercase
from textFile import Encrypted_text
import matplotlib.pyplot as plt


alphabets = ascii_lowercase + ascii_uppercase
lower_case = ascii_lowercase


def count_value(text_file):
    """
    Parameter: a string of alphanumeric values

    returns a dictionary with key as each indiviual alphabets with the value as number of times it occurs 
    """

    lower_text = text_file.lower()
    frequencies = {}

    for i in lower_text:

        if i in alphabets:

            if i not in frequencies:
                frequencies[i] = 1

            else:
                frequencies[i] += 1

    return frequencies


def sort_dict(dict1):
    """
    Takes a dictionary
    Returns a dictionary
    """

    new_dict = {}
    alist = []

    for keys in dict1:
        alist.append(keys)

    alist.sort()
    
    for i in alist:
        new_dict[i] = dict1[i]
    return new_dict


def most_occured(dict):
    """
    Takes a dictionary
    Returns a char representing the most occured alphabet in the given corpus.
    """

    max = dict['e']
    max_alpha = 'e'

    for i, j in zip(dict.values(), dict.keys()):

        if max < i:
            max = i
            max_alpha = j
    
    return max_alpha


def main(str_text):
    """
    When given a corpus, it returns the frequencies of all
    alphabets, in a sorted format.
    """

    frequencies = count_value(str_text)
    sorted_data = sort_dict(frequencies)

    return sorted_data

frequencies = count_value(Encrypted_text)
sorted_data = sort_dict(frequencies)
highest_recurred = most_occured(sorted_data)

D = main(Encrypted_text)

plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.xlabel('alphabets')
plt.ylabel('Times the char repeated')
plt.legend()
plt.show()

substitudedValue = lower_case.index(highest_recurred) - 5

print(f"\nMost occured letter is: {highest_recurred}")
# We know that the in the English Alphabet the letter with the highest frequency is usually the letter 'e'")
# Hence, the shift in the letter leads us to the change in substitution.") 

print("Here the letters are substitued by:", substitudedValue + 1)
print("The message, after decryption is : ", Encrypter(Encrypted_text, - substitudedValue - 1))