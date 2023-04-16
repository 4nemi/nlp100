import subprocess

#col1.txtとcol2.txtをタブ区切りで結合
with open("col1.txt") as f, open("col2.txt") as g, open("merged.txt", "w") as h:
    for col1, col2 in zip(f, g):
        h.write(col1.rstrip() + "\t" + col2)

