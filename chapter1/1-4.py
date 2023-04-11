sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
sentence = sentence.replace('.', '')
words = sentence.split()

element_dict = {}
for i, word in enumerate(words, 1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        element_dict[word[:1]] = i
    else:
        element_dict[word[:2]] = i

print(element_dict)