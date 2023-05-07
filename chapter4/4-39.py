from get_morphemes import get_morphemes
from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

sentences = get_morphemes()
#単語の出現頻度順位を横軸、出現頻度を縦軸として、両対数グラフをプロット
word_count = defaultdict(int)
for sentence in sentences:
    for morpheme in sentence:
        word_count[morpheme['surface']] += 1
word_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)

plt.scatter([i+1 for i in range(len(word_count))], [x[1] for x in word_count])
plt.xscale('log')
plt.yscale('log')
plt.savefig('4-39.png')
