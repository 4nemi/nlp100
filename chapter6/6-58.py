import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import joblib
import numpy as np
import matplotlib.pyplot as plt

#正則化パラメータを調整して学習
def train():
    #データの読み込み
    df_train = pd.read_csv('train.feature.txt', sep='\t')
    df_valid = pd.read_csv('valid.feature.txt', sep='\t')
    df_test = pd.read_csv('test.feature.txt', sep='\t')
    #学習データの特徴量と正解ラベルを指定
    X_train = df_train.drop('CATEGORY', axis=1)
    Y_train = df_train['CATEGORY']
    #検証データの特徴量と正解ラベルを指定
    X_valid = df_valid.drop('CATEGORY', axis=1)
    Y_valid = df_valid['CATEGORY']
    #評価データの特徴量と正解ラベルを指定
    X_test = df_test.drop('CATEGORY', axis=1)
    Y_test = df_test['CATEGORY']
    
    acc_train = []
    acc_valid = []
    acc_test = []

    for c in np.logspace(-5, 4, 10, base=10):
        #モデルの学習
        model = LogisticRegression(random_state=42, max_iter=10000, C=c)
        model.fit(X_train, Y_train)

        #学習データの予測結果を取得
        Y_pred_train = model.predict(X_train)

        #学習データの正解率を表示
        train_acc = accuracy_score(Y_train, Y_pred_train)
        acc_train.append(train_acc)
        print(f'C={c} 正解率(学習データ): {train_acc}')


        #検証データの予測結果を取得
        Y_pred = model.predict(X_valid)

        #検証データの正解率を表示
        valid_acc = accuracy_score(Y_valid, Y_pred)
        acc_valid.append(valid_acc)
        print(f'C={c} 正解率(検証データ): {valid_acc}')

        #評価データの予測結果を取得
        Y_pred = model.predict(X_test)

        #評価データの正解率を表示
        test_acc = accuracy_score(Y_test, Y_pred)
        acc_test.append(test_acc)
        print(f'C={c} 正解率(評価データ): {test_acc}')

        #モデルを保存
        joblib.dump(model, f'model_{c}.joblib')
    
    #グラフの描画
    plt.plot(np.logspace(-5, 4, 10, base=10), acc_train, label='train')
    plt.plot(np.logspace(-5, 4, 10, base=10), acc_valid, label='valid')
    plt.plot(np.logspace(-5, 4, 10, base=10), acc_test, label='test')
    plt.xscale('log')
    plt.xlabel('C')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('logistic_regression.png')

if __name__ == '__main__':
    train()
