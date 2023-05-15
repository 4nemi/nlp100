from morph import Morph
from chunk import Chunk
import pydot

#与えられた文の係り受け木を有向グラフとして可視化する
def visualize_dependency_structure(sentence):
    graph = pydot.Dot(graph_type="digraph")
    for chunk in sentence:
        if chunk.dst != -1:
            src = "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])
            dst = "".join([morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != "記号"])
            graph.add_edge(pydot.Edge(src, dst))
    return graph

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

    for i, sentence in enumerate(sentences):
        if i == 7:
            graph = visualize_dependency_structure(sentence)
            graph.write_png("5-47.png", prog="dot")
            break