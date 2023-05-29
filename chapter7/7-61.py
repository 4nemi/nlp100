from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

#"United States"と"U.S."のコサイン類似度を計算
print(model.similarity('United_States', 'U.S.'))