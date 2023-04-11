def cipher(text):
    return  ''.join([chr(219-ord(c)) if c.islower() else c for c in text])

text = 'I am an NLPer'
print(cipher(text))