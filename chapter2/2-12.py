import subprocess

with open("popular-names.txt") as f:
    with open("col1.txt", "w") as g, open("col2.txt", "w") as h:
        for line in f:
            cols = line.split("\t")
            g.write(cols[0] + "\n")
            h.write(cols[1] + "\n")

#subprocess.run(["cut", "-f", "1", "popular-names.txt"])