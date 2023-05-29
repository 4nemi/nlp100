from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

#"United States"とコサイン類似度が高い10語とその類似度を表示
print(model.most_similar(positive=['United_States'], topn=10))