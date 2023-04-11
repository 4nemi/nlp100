def character_n_gram(text, N):
    text = text.replace(' ', '')
    return [text[i:i+N] for i in range(len(text)-N+1)]

X = character_n_gram('paraparaparadise', 2)
Y = character_n_gram('paragraph', 2)

print(f'和集合: {set(X) | set(Y)}')
print(f'積集合: {set(X) & set(Y)}')
print(f'差集合: {set(X) - set(Y)}')

if 'se' in set(X):
    print('Xにseは含まれる')
else:
    print('Xにseは含まれない')

if 'se' in set(Y):
    print('Yにseは含まれる')
else:
    print('Yにseは含まれない')