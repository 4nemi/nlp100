#単語アナロジーの評価データをダウンロード
from gensim.models import KeyedVectors
import subprocess
from tqdm import tqdm

subprocess.run(['wget', 'http://download.tensorflow.org/data/questions-words.txt'])
#単語アナロジーの評価データを読み込み、表示
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

with open('questions-words.txt') as f, open('questions-words-ans.txt', 'w') as f_ans:
    for line in tqdm(f):
        line = line.split()
        if line[0] == ':':
            category = line[1]
        if len(line) == 4:
            ans = model.most_similar(positive=[line[1], line[2]], negative=[line[0]], topn=1)
            similarity = ans[0][1]
            f_ans.write("{} {} {} {}\n".format(category, line[3], ans[0][0], similarity))
