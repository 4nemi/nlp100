from morph import Morph
from chunk import Chunk
"""
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．
・動詞を含む文節において，最左の動詞の基本形を述語とする
・述語に係る助詞を格とする
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
"""

def extract_case_pattern(sentence):
    for chunk in sentence:
        #chunkに動詞が含まれているか
        if "動詞" in [morph.pos for morph in chunk.morphs]:
            #chunkに含まれる最左の動詞の基本形
            predicate = [morph.base for morph in chunk.morphs if morph.pos == "動詞"][-1]
            #動詞に係る文節の助詞のリスト
            cases = []
            for src in chunk.srcs:
                cases += [morph.surface for morph in sentence[src].morphs if morph.pos == "助詞"]
            if cases:
                print(f"{predicate}\t{' '.join(sorted(cases))}")

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



