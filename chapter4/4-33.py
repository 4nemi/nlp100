from get_morphemes import get_morphemes

sentences = get_morphemes()
#AのBのパターンをすべて抽出
patterns = set()
aandb = []
for sentence in sentences:
    for morpheme in sentence:
        if morpheme['pos'] == '名詞':
            aandb.append(morpheme['surface'])
        elif morpheme['surface'] == 'の':
            if len(aandb) > 0:
                aandb.append(morpheme['surface'])
        else:
            #len == 3かつaandb[1] == 'の'のときのみパターンに追加
            if len(aandb) == 3 and aandb[1] == 'の':
                patterns.add(''.join(aandb))
            aandb = []
print(patterns)
