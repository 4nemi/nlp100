#ロジスティック回帰モデルの学習
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

def train():
    #データの読み込み
    df_train = pd.read_csv('train.feature.txt', sep='\t')
    df_valid = pd.read_csv('valid.feature.txt', sep='\t')

    #学習データの特徴量と正解ラベルを指定
    X_train = df_train.drop('CATEGORY', axis=1)
    Y_train = df_train['CATEGORY']

    #モデルの学習
    model = LogisticRegression(random_state=42, max_iter=10000)
    model.fit(X_train, Y_train)

    #学習データの予測結果を取得
    Y_pred_train = model.predict(X_train)

    #学習データの正解率を表示
    print(f'正解率(学習データ): {accuracy_score(Y_train, Y_pred_train)}')


    #検証データの特徴量と正解ラベルを指定
    X_valid = df_valid.drop('CATEGORY', axis=1)
    Y_valid = df_valid['CATEGORY']

    #検証データの予測結果を取得
    Y_pred = model.predict(X_valid)

    #検証データの正解率を表示
    print(f'正解率(検証データ): {accuracy_score(Y_valid, Y_pred)}')

    #モデルを保存
    joblib.dump(model, 'model.joblib')

    #検証と学習の予測値を保存
    Y_pred_train = pd.DataFrame(Y_pred_train)
    Y_pred = pd.DataFrame(Y_pred)
    Y_pred_train.to_csv('train_pred.txt', index=False, header=None)
    Y_pred.to_csv('valid_pred.txt', index=False, header=None)


if __name__ == '__main__':
    train()