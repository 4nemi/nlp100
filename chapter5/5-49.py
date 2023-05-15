from morph import Morph
from chunk import Chunk
"""
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出
問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を” -> “で連結して表現する
文節i
とj
に含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

文節i
から構文木の根に至る経路上に文節j
が存在する場合: 文節i
から文節j
のパスを表示
上記以外で，文節i
と文節j
から構文木の根に至る経路上で共通の文節k
で交わる場合: 文節i
から文節k
に至る直前のパスと文節j
から文節k
に至る直前までのパス，文節k
の内容を” | “で連結して表示
"""

def extract_shortest_path(sentence):
    for i, chunk in enumerate(sentence):
        if "名詞" in [morph.pos for morph in chunk.morphs]:
            for j in range(i+1, len(sentence)):
                if "名詞" in [morph.pos for morph in sentence[j].morphs]:
                    path_i = ["".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])]
                    dst_i = chunk.dst
                    while dst_i != -1:
                        path_i.append("".join([morph.surface for morph in sentence[dst_i].morphs if morph.pos != "記号"]))
                        dst_i = sentence[dst_i].dst
                    path_j = ["".join([morph.surface for morph in sentence[j].morphs if morph.pos != "記号"])]
                    dst_j = sentence[j].dst
                    while dst_j != -1:
                        path_j.append("".join([morph.surface for morph in sentence[dst_j].morphs if morph.pos != "記号"]))
                        dst_j = sentence[dst_j].dst
                    if path_i[0] == path_j[0]:
                        path = path_i[1:]
                        path.reverse()
                        path.append("X")
                        path.reverse()
                        path += path_j[1:]
                        print(" -> ".join(path))
                        break
                    else:
                        for k in range(len(path_i)):
                            if path_i[k] in path_j:
                                path = path_i[:k]
                                path.reverse()
                                path.append("X")
                                path.reverse()
                                path += path_j[:path_j.index(path_i[k])]
                                path.append("Y")
                                path += path_j[path_j.index(path_i[k])+1:]
                                print(" -> ".join(path))
                                break
                        break

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

    extract_shortest_path(sentences[2])