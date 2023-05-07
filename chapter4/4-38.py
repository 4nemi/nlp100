from get_morphemes import get_morphemes
from collections import defaultdict
from matplotlib import pyplot as plt
import japanize_matplotlib

sentences = get_morphemes()
#単語の出現頻度のヒストグラムを描く
word_count = defaultdict(int)
for sentence in sentences:
    for morpheme in sentence:
        word_count[morpheme['surface']] += 1
word_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)

#横軸は出現頻度、縦軸は出現頻度をとる単語の数
plt.hist([x[1] for x in word_count[:100]], bins=10)
plt.savefig('4-38.png')