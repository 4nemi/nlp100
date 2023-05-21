#特徴量の重みの確認
import pandas as pd
import joblib

#モデルの読み込み
model = joblib.load('model.joblib')

#重みを取得
weights = model.coef_

#特徴量名を取得
df_train = pd.read_csv('train.feature.txt', sep='\t')
df_train = df_train.drop('CATEGORY', axis=1)
features = df_train.columns

#カテゴリごとの重みを昇順と降順で表示
for i, category in enumerate(model.classes_):
    print(f'【カテゴリ】{category}')
    print('  重みTOP10')
    print(pd.DataFrame(weights[i], features).sort_values(by=0, ascending=False).head())
    print('  重みBOTTOM10')
    print(pd.DataFrame(weights[i], features).sort_values(by=0, ascending=False).tail())
    print('')
