from morph import Morph
from chunk import Chunk
"""
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

・項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
・述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
"""

def extract_case_and_phrase(sentence):
    for chunk in sentence:
        if "動詞" in [morph.pos for morph in chunk.morphs]:
            predicate = [morph.base for morph in chunk.morphs if morph.pos == "動詞"][0]
            cases = []
            phrases = []
            for src in chunk.srcs:
                cases += [morph.surface for morph in sentence[src].morphs if morph.pos == "助詞"]
                phrases += [morph.surface for morph in sentence[src].morphs if morph.pos != "記号"]
            if cases:
                print(f"{predicate}\t{' '.join(sorted(cases))}\t{' '.join(phrases)}")

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
                
    extract_case_and_phrase(sentences[7])