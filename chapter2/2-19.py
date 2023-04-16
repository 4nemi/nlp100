from collections import Counter

with open("popular-names.txt") as f:
    col1 = [line.split("\t")[0] for line in f]
    c = Counter(col1)
sorted_c = sorted(c.items(), key=lambda x: x[1], reverse=True)

for k, v in sorted_c:
    print(k, v)