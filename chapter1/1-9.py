import random

def Typoglycemia(text):
    result = []
    for word in text.split():
        if len(word) > 4:
            word = word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1]
        result.append(word)
    return ' '.join(result)

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(text))

