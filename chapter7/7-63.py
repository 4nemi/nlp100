from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

#"Spain"-"Madrid"+"Athens"のベクトルを計算
print(model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10))