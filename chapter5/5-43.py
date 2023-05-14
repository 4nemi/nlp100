from morph import Morph
from chunk import Chunk
#名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ

def extract_noun_verb(sentence):
    for chunk in sentence:
        if chunk.dst != -1:
            if "名詞" in [morph.pos for morph in chunk.morphs] and "動詞" in [morph.pos for morph in sentence[chunk.dst].morphs]:
                print(f"{''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])}\t{''.join([morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != '記号'])}")

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
        extract_noun_verb(sentence)        