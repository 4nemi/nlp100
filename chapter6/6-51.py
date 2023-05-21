import pandas as pd
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import re

#データのへッダーを設定
columns = ['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP']
#データを読み込む
df_train = pd.read_csv('train.txt', sep='\t', header=None, names=columns)
df_valid = pd.read_csv('valid.txt', sep='\t', header=None, names=columns)
df_test = pd.read_csv('test.txt', sep='\t', header=None, names=columns)

#textデータの前処理
def preprocessing_text(text):
    table = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    text = text.translate(table)
    text = text.lower()
    #数字を0に置き換える
    text = re.sub(r'\d+', '0', text)
    return text

#特徴量を抽出する
def extract_features(df):
    #publisherを数値に変換
    df['PUBLISHER'] = df['PUBLISHER'].fillna('NaN')
    le = preprocessing.LabelEncoder()
    le.fit(df['PUBLISHER'])
    df['PUBLISHER'] = le.transform(df['PUBLISHER'])

    #storyを数値に変換
    df['STORY'] = df['STORY'].fillna('NaN')
    le = preprocessing.LabelEncoder()
    le.fit(df['STORY'])
    df['STORY'] = le.transform(df['STORY'])
    #カテゴリーを数値に変換
    mapping = {'b': 0, 't': 1, 'e': 2, 'm': 3}
    df['CATEGORY'] = df['CATEGORY'].map(mapping)

    #不要な列を削除
    df = df.drop(['ID', 'URL', 'HOSTNAME', 'TIMESTAMP'], axis=1)
    return df

def get_tfidf(df):
    #TITLEの前処理
    df['TITLE'] = df['TITLE'].map(preprocessing_text)
    #TITLEをベクトル化
    vectorizer = TfidfVectorizer(use_idf=True, min_df=10, max_df=0.5)
    X = vectorizer.fit_transform(df['TITLE'])
    #TFIDFの結果をデータフレームに格納
    df_tfidf = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    #データフレームを結合
    df = pd.concat([df, df_tfidf], axis=1)
    return df


#特徴量を抽出
df_train = extract_features(df_train)
df_valid = extract_features(df_valid)
df_test = extract_features(df_test)

#TFIDFを計算
df = pd.concat([df_train, df_valid, df_test], axis=0).reset_index(drop=True)
df = get_tfidf(df)
df.drop('TITLE', axis=1, inplace=True)
df_train = df[:len(df_train)]
df_valid = df[len(df_train):len(df_train)+len(df_valid)]
df_test = df[len(df_train)+len(df_valid):]

#txtファイルに保存
df_train.to_csv('train.feature.txt', sep='\t', index=False)
df_valid.to_csv('valid.feature.txt', sep='\t', index=False)
df_test.to_csv('test.feature.txt', sep='\t', index=False)