import pandas as pd
from sklearn.model_selection import train_test_split
from gensim.models import KeyedVectors
import string
import torch

df = pd.read_csv('../chapter6/newsCorpora.csv', sep='\t', header=None, names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])
df = df[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]
df = df.sample(frac=1, random_state=42)

train, valid_test = train_test_split(df, test_size=0.2, random_state=42)
valid, test = train_test_split(valid_test, test_size=0.5, random_state=42)

#単語ベクトルを読み込む
model = KeyedVectors.load_word2vec_format('../chapter7/GoogleNews-vectors-negative300.bin.gz', binary=True)

def transform(text):
    #textを受け取り、vectorに変換する関数
    text = text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))) #句読点をスペースに置換
    text = text.split() #空白で分割
    text = [token for token in text if token in model] #単語ベクトルが存在する単語のみを取得
    return torch.tensor(model[text], dtype=torch.float32).mean(dim=0) #平均ベクトルをtensorとして返す

#各データを変換
train_x = torch.stack([transform(text) for text in train['TITLE']])
valid_x = torch.stack([transform(text) for text in valid['TITLE']])
test_x = torch.stack([transform(text) for text in test['TITLE']])

#ラベルのベクトルを作成
train_y = torch.tensor([['b', 't', 'e', 'm'].index(category) for category in train['CATEGORY']])
valid_y = torch.tensor([['b', 't', 'e', 'm'].index(category) for category in valid['CATEGORY']])
test_y = torch.tensor([['b', 't', 'e', 'm'].index(category) for category in test['CATEGORY']])

#データを保存
torch.save(train_x, 'train_x.pt')
torch.save(valid_x, 'valid_x.pt')
torch.save(test_x, 'test_x.pt')
torch.save(train_y, 'train_y.pt')
torch.save(valid_y, 'valid_y.pt')
torch.save(test_y, 'test_y.pt')
