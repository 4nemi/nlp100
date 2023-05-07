from get_morphemes import get_morphemes

sentences = get_morphemes()

#名詞の連接を最長一致で抽出
nouns = []
for sentence in sentences:
    noun = []
    for morpheme in sentence:
        if morpheme['pos'] == '名詞':
            noun.append(morpheme['surface'])
        else:
            if len(noun) > 1:
                nouns.append(''.join(noun))
            noun = []
print(nouns)