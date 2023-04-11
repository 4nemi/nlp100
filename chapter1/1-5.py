def character_n_gram(text, N):
    text = text.replace(' ', '')
    return [text[i:i+N] for i in range(len(text)-N+1)]

def word_n_gram(text, N):
    text = text.split()
    return [text[i:i+N] for i in range(len(text)-N+1)]

text = 'I am an NLPer'
print(character_n_gram(text, 2))
print(word_n_gram(text, 2))