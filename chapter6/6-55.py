from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():
    #学習データの予測値を読み込む
    df_train_pred = pd.read_csv('train_pred.txt', header=None)
    df_train = pd.read_csv('train.feature.txt', sep='\t')
    cm_train = confusion_matrix(df_train['CATEGORY'], df_train_pred[0])

    #テストデータの予測値を読み込む
    df_test_pred = pd.read_csv('pred_proba.csv', header=None)
    df_test = pd.read_csv('test.feature.txt', sep='\t')
    cm_test = confusion_matrix(df_test['CATEGORY'], df_test_pred.idxmax(axis=1))

    #学習データの混同行列を表示
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm_train, annot=True, cmap='Blues')
    #保存
    plt.savefig('confusion_matrix_train.png')

    #テストデータの混同行列を表示
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm_test, annot=True, cmap='Blues')
    #保存
    plt.savefig('confusion_matrix_test.png')

if __name__ == '__main__':
    main()
