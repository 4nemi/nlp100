from morph import Morph
from chunk import Chunk
"""
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
"""

def extract_case_pattern(sentence):
    for chunk in sentence:
        #chunkに動詞が含まれているか
        if "動詞" in [morph.pos for morph in chunk.morphs]:
            #chunkに含まれる最左の動詞の基本形
            predicate = [morph.base for morph in chunk.morphs if morph.pos == "動詞"][0]
            #動詞に係る文節の助詞のリスト
            cases = []
            #動詞に係る文節のリスト
            phrases = []
            flag = False
            for src in chunk.srcs:
                #助詞とその文節を抽出
                cases += [morph.surface for morph in sentence[src].morphs if morph.pos == "助詞"]
                phrases += [morph.surface for morph in sentence[src].morphs if morph.pos != "記号"]

                #サ変接続名詞 + を(助詞)の文節のみを抽出
                if "サ変接続" in [morph.pos1 for morph in sentence[src].morphs] and "を" in [morph.surface for morph in sentence[src].morphs]:
                    #サ変接続名詞 + を(助詞)を抽出
                    sahen_wo = [morph.surface for morph in sentence[src].morphs if morph.pos1 == "サ変接続" or morph.surface == "を"]
                    flag = True
                if flag and cases != []:
                    #サ変接続名詞とをphrasesとcasesから削除
                    
                    print(f"{''.join(sahen_wo+[predicate])}\t{''.join(sorted(cases))}\t{''.join(phrases)}")
                    flag = False
                    cases = []
                    phrases = []
                    

if __name__ == "__main__":
    with open("ai.ja.txt.parsed") as f:
        sentences = []
        sentence = []
        chunk = None
        for line in f:
            if line[0] == '*':
                if chunk:
                    sentence.append(chunk)
                chunk = Chunk(line.split())
            elif line != 'EOS\n':
                chunk.add_morph(Morph(line))
            else:
                if chunk:
                    sentence.append(chunk)
                for i, src in enumerate(sentence):
                    if src != None and src.dst != -1:
                        sentence[src.dst].add_src(i)
                sentences.append(sentence)
                sentence = []
                chunk = None

    for sentence in sentences:
        extract_case_pattern(sentence)