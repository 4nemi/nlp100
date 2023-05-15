from morph import Morph
from chunk import Chunk

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