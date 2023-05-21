import subprocess
import pandas as pd
from sklearn.model_selection import train_test_split

#News Aggregator Data Setをダウンロード
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00359/NewsAggregatorDataset.zip'
subprocess.run(['curl', '-O', url])

#zipファイルを解凍
subprocess.run(['unzip', 'NewsAggregatorDataset.zip'])

#データを読み込む
df = pd.read_csv('newsCorpora.csv', sep='\t', header=None)

#publisherが”Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com”, “Daily Mail”のデータを抽出
df = df[df[3].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]

#データを検証データ、学習データ、テストデータに分割
df = df.sample(frac=1, random_state=42)
train, valid_test = train_test_split(df, test_size=0.2, random_state=42)
valid, test = train_test_split(valid_test, test_size=0.5, random_state=42)

#それぞれのデータをtxtファイルに保存
train.to_csv('train.txt', sep='\t', index=False, header=None)
valid.to_csv('valid.txt', sep='\t', index=False, header=None)
test.to_csv('test.txt', sep='\t', index=False, header=None)