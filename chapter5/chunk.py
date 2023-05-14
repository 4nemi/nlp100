from morph import Morph
#文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）の

class Chunk:
    def __init__(self, chunk):
        self.morphs = []
        self.dst = int(chunk[2].rstrip('D'))
        self.srcs = []

    def add_morph(self, morph):
        self.morphs.append(morph)

    def add_src(self, src):
        self.srcs.append(src)

#ai.ja.txt.parsedを読み込み、各文をChunkオブジェクトのリストとして表現
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
                if src.dst != -1:
                    sentence[src.dst].add_src(i)
            sentences.append(sentence)
            sentence = []
            chunk = None

if __name__ == "__main__":
    #冒頭の説明文の文節の文字列と係り先文節番号を表示
    for i, chunk in enumerate(sentences[2]):
        print(f"chunk {i}:")
        print(f"srcs: {chunk.srcs}")
        print(f"  morphs: {[vars(morph) for morph in chunk.morphs]}")
        print(f"  dst: {chunk.dst}")
