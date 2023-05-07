from get_morphemes import get_morphemes
from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

sentences = get_morphemes()
#「猫」と共起する単語を抽出
co_occurrence = defaultdict(int)

for sentence in sentences:
    for morpheme in sentence:
        if morpheme['surface'] == '猫':
            for morpheme2 in sentence:
                if morpheme2['surface'] != '猫' and morpheme2['pos'] in ['名詞', '動詞', '形容詞'] and morpheme2['pos1'] != '非自立':
                    co_occurrence[morpheme2['surface']] += 1
#出現頻度の高い順に並べる
co_occurrence = sorted(co_occurrence.items(), key=lambda x:x[1], reverse=True)
plt.bar([x[0] for x in co_occurrence[:10]], [x[1] for x in co_occurrence[:10]])
plt.savefig('4-37.png')

