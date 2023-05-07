import subprocess

def get_morphemes():
    with open('neko.txt.mecab') as f:
        #各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現する
        sentences = []
        sentence = []
        for line in f:
            #空行はスキップ
            if line == '\n':
                continue
            if line == 'EOS\n':
                #文の終端で，形態素のリストを文のリストに追加
                sentences.append(sentence)
                #次の文のために，形態素のリストと文のリストを初期化
                sentence = []
                continue
            #行末の改行を削除
            line = line.rstrip('\n')
            #タブで区切って表層形はsurfaceに，それ以外はfeatureに代入
            surface, feature = line.split('\t')
            if surface == '':
                continue
            #featureをカンマで区切ってそれぞれpos, pos1, pos2, pos3, conjugation, inflection, original, reading, pronunciationに代入
            feature = feature.split(',')
            #マッピング型に格納
            morpheme = {'surface': surface, 'base': feature[6], 'pos': feature[0], 'pos1': feature[1]}
            sentence.append(morpheme)
    return sentences
    
if __name__ == '__main__':
    #neko.txtをダウンロード
    subprocess.run('wget -nc -P . https://nlp100.github.io/data/neko.txt', shell=True)
    #neko.txtをmecabで形態素解析してneko.txt.mecabに保存
    subprocess.run('mecab < neko.txt > neko.txt.mecab', shell=True)
    #neko.txt.mecabを読み込んで形態素解析結果をリストに格納
    sentences = get_morphemes()
    #形態素解析結果の1文を表示
    print(sentences[2])