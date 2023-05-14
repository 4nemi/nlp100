#形態素を表すクラスMorphを実装

class Morph:
    def __init__(self, morpheme):
        surface, attribute = morpheme.split('\t')
        attribute = attribute.split(',')
        self.surface = surface
        self.base = attribute[6]
        self.pos = attribute[0]
        self.pos1 = attribute[1]

#ai.ja.txt.parsedを読み込み、各文をMorphオブジェクトのリストとして表現
with open("ai.ja.txt.parsed") as f:
    #各文をMorphオブジェクトのリストとして表現
    sentences = []
    sentence = []
    for line in f:
        if line[0] == '*':
            continue
        elif line != 'EOS\n':
            sentence.append(Morph(line))
        else:
            sentences.append(sentence)
            sentence = []

if __name__ == "__main__":
    #冒頭の説明文の形態素列を表示
    for morph in sentences[2]:
        print(vars(morph))