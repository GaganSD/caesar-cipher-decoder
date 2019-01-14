from cipher import cipherDecrypt
import string
import matplotlib.pyplot as plt

alphabets = string.ascii_lowercase + string.ascii_uppercase
lower_case = string.ascii_lowercase


def count_value(text_file):

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
    new_dict = {}
    alist = []
    
    for keys in dict1:
        alist.append(keys)
    alist.sort()
    
    for i in alist:
        new_dict[i] = dict1[i]
    
    return new_dict


def most_occured(dict):
    max = dict['e']
    max_alpha = 'e'

    for i, j in zip(dict.values(), dict.keys()):

        if max < i:
            max = i
            max_alpha = j
    
    return max_alpha


def main(dictionary):

    frequencies = count_value(dictionary)
    sorted_data = sort_dict(frequencies)
    return sorted_data


frequencies = count_value(Encrypted_text)
sorted_data = sort_dict(frequencies)
highest_recurred = most_occured(sorted_data)


Encrypted_text = """
WKH ERDVWLQJ WUDYHOOHU


D Pdq rqfh zhqw deurdg rq klv wudyhov, dqg zkhq kh fdph krph kh
kdg zrqghuixo wdohv wr whoo ri wkh wklqjv kh kdg grqh lq iruhljq
frxqwulhv. Dprqj rwkhu wklqjv, kh vdlg kh kdg wdnhq sduw lq d
mxpslqj-pdwfk dw Ukrghv, dqg kdg grqh d zrqghuixo mxps zklfk qr rqh
frxog ehdw. "Mxvw jr wr Ukrghv dqg dvn wkhp," kh vdlg; "hyhub rqh zloo
whoo brx lw'v wuxh." Exw rqh ri wkrvh zkr zhuh olvwhqlqj vdlg, "Li brx
fdq mxps dv zhoo dv doo wkdw, zh qhhgq'w jr wr Ukrghv wr suryh lw.
Ohw'v mxvw lpdjlqh wklv lv Ukrghv iru d plqxwh: dqg qrz--mxps!"

    Ghhgv, qrw zrugv.
"""

D = main(Encrypted_text)

plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.xlabel('alphabets')
plt.ylabel('Times the char repeated')
plt.legend()
plt.show()

substitudedValue = lower_case.index(highest_recurred) - 5

print(f"\nThe letter that occured the most is : {highest_recurred}")
print("\nWe know that the in the English Alphabet the letter with the highest frequency is usually the letter 'e'")
print("\nHence, the shift in the letter leads us to the change in substitution.") 
print("\nHere the letters are substitued by:", substitudedValue)

print("The message, after decryption is : ", cipherDecrypt(Encrypted_text, substitudedValue))