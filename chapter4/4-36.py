from get_morphemes import get_morphemes
from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib
sentences = get_morphemes()

#出現頻度の上位10語とその出現頻度を棒グラフで表示
word_count = defaultdict(int)
for sentence in sentences:
    for morpheme in sentence:
        word_count[morpheme['surface']] += 1
word_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)

plt.bar([x[0] for x in word_count[:10]], [x[1] for x in word_count[:10]])
plt.savefig('4-36.png')
