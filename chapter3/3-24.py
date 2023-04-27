import re
with open("uk.txt") as f:
    uk = f.read()

r = "\[\[ファイル:(.*?)(?:\|.*)\]\]"
file = re.findall(r, uk)
for f in file:
    print(f)