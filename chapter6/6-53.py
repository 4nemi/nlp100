#予測確率を計算する
import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

def predict():
    #データの読み込み
    df_test = pd.read_csv('test.feature.txt', sep='\t')

    #モデルの読み込み
    model = joblib.load('model.joblib')

    #テストデータの特徴量と正解ラベルを指定
    X_test = df_test.drop('CATEGORY', axis=1)
    Y_test = df_test['CATEGORY']

    #テストデータの予測結果を取得
    Y_pred = model.predict(X_test)

    #テストデータの正解率を表示
    print(f'正解率：{accuracy_score(Y_test, Y_pred)}')

    #テストデータの予測確率を取得
    Y_pred_proba = model.predict_proba(X_test)

    #予測確率をデータフレームに変換
    df_pred_proba = pd.DataFrame(Y_pred_proba)

    #予測確率をcsvファイルに保存
    df_pred_proba.to_csv('pred_proba.csv', index=False, header=None)

if __name__ == '__main__':
    predict()