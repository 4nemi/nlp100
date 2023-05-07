from get_morphemes import get_morphemes
from collections import defaultdict

sentences = get_morphemes()
#単語の出現頻度を求める
word_count = defaultdict(int)
for sentence in sentences:
    for morpheme in sentence:
        word_count[morpheme['surface']] += 1
#出現頻度の高い順に並べる
word_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
print(word_count[:10])
