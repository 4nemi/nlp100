sentence  = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
sentence  = sentence.replace(',', '').replace('.', '')
words  = sentence.split()
word_length = [len(word) for word in words]
print(word_length)