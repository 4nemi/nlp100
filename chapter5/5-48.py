from morph import Morph
from chunk import Chunk
""""
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を” -> “で連結する
"""

def extract_path(sentence):
    for chunk in sentence:
        if "名詞" in [morph.pos for morph in chunk.morphs]:
            path = ["".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])]
            dst = chunk.dst
            while dst != -1:
                path.append("".join([morph.surface for morph in sentence[dst].morphs if morph.pos != "記号"]))
                dst = sentence[dst].dst
            print(" -> ".join(path))

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
        extract_path(sentence)