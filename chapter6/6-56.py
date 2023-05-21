#適合率，再現率，F1スコアを求める
#カテゴリごとの性能をマイクロ平均（micro-average）とマクロ平均（macro-average）で統合
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd

def main():
    #テストデータの予測値を読み込む
    df_test_pred = pd.read_csv('pred_proba.csv', header=None)
    df_test = pd.read_csv('test.feature.txt', sep='\t')

    #テストデータの予測値をラベルに変換
    test_pred = df_test_pred.idxmax(axis=1).values

    test_true = df_test['CATEGORY'].values

    #カテゴリごとに適合率，再現率，F1スコアを計算
    precision = precision_score(test_true, test_pred, average=None)
    recall = recall_score(test_true, test_pred, average=None)
    f1 = f1_score(test_true, test_pred, average=None)

    #マイクロ平均を計算
    precision_micro = precision_score(test_true, test_pred, average='micro')
    recall_micro = recall_score(test_true, test_pred, average='micro')
    f1_micro = f1_score(test_true, test_pred, average='micro')

    #マクロ平均を計算
    precision_macro = precision_score(test_true, test_pred, average='macro')
    recall_macro = recall_score(test_true, test_pred, average='macro')
    f1_macro = f1_score(test_true, test_pred, average='macro')

    #結果を表示
    print(f'適合率（マイクロ平均）：{precision_micro:.3f}')
    print(f'再現率（マイクロ平均）：{recall_micro:.3f}')
    print(f'F1スコア（マイクロ平均）：{f1_micro:.3f}')

    print(f'適合率（マクロ平均）：{precision_macro:.3f}')
    print(f'再現率（マクロ平均）：{recall_macro:.3f}')
    print(f'F1スコア（マクロ平均）：{f1_macro:.3f}')

if __name__ == '__main__':
    main()


