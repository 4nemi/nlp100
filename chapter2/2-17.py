with open("popular-names.txt") as f:
    col1 = [line.split("\t")[0] for line in f]

col1 = set(col1)
print(col1)