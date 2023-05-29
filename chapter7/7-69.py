#国名に関するベクトルをt-SNEで可視化する
import numpy as np
import bhtsne
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

embeddings = bhtsne.tsne(np.array(countries_vec).astype(np.float64), dimensions=2, rand_seed=123)
plt.figure(figsize=(10, 10))
plt.scatter(np.array(embeddings).T[0], np.array(embeddings).T[1])
for (x, y), name in zip(embeddings, countries):
    plt.annotate(name, (x, y))
plt.show()