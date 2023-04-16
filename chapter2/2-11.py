import subprocess

with open("popular-names.txt", "r") as f:
    with open("popular-names-converted.txt", "w") as g:
        for line in f:
            line = line.replace("\t", " ")
            g.write(line)