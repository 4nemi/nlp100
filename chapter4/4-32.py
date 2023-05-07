from get_morphemes import get_morphemes

sentences = get_morphemes()
#動詞の基本形をすべて抽出
verbs = set()
for sentence in sentences:
    for morpheme in sentence:
        if morpheme['pos'] == '動詞':
            verbs.add(morpheme['base'])
print(verbs)