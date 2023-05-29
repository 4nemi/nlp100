from morph import Morph
from chunk import Chunk

def extract_shortest_path(sentence):
    for i, chunk in enumerate(sentence):
        if "名詞" in [morph.pos for morph in chunk.morphs]:
            path_X = []
            idx_X = []
            for j in range(i+1, len(sentence)):
                if "名詞" in [morph.pos for morph in sentence[j].morphs]:
                    path_Y = []
                    idx_Y = []
                    dst_i = i
                    dst_j = j
                #Xから根に至るパスを作成
                    cnt = 0
                    while dst_i != -1:
                        idx_X.append(dst_i)
                        path_X.append(''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sentence[dst_i].morphs]))
                        if sentence[dst_i].dst >= j and cnt == 0:
                            toY = dst_i
                            cnt += 1
                        dst_i = sentence[dst_i].dst
                #Yから根に至るパスを作成
                    while dst_j != -1:
                        idx_Y.append(dst_j)
                        path_Y.append(''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence[dst_j].morphs]))
                        dst_j = sentence[dst_j].dst
                #XとYの最短パスを求める
                    shortest_path = []
                    #XがYに直接かかっている場合
                    if j in idx_X:
                        shortest_path = path_X[:idx_X.index(j)+1]
                        print(' -> '.join(shortest_path))
                    #XとYが共通の係り先を持つ場合
                    else:
                        for p in idx_Y:
                            if p in idx_X:
                                shortest_path = ' -> '.join(path_X[:idx_X.index(toY)+1]) + ' | ' + ' -> '.join(path_Y[:idx_Y.index(p)+1])
                                print(shortest_path)
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