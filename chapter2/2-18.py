with open("popular-names.txt") as f, open("popular-names-sorted.txt", "w") as g:
    lines = f.readlines()
    sorted_lines = sorted(lines, key=lambda x: x.split("\t")[2], reverse=True)
    for line in sorted_lines:
        g.write(line)
