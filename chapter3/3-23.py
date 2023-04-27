import re
#セクション構造を抽出
with open("uk.txt") as f:
    uk = f.read()
pattern = r"(={2,})(.*?)=+"
section = re.findall(pattern, uk)
for s in section:
    print(s[1], len(s[0])-1)
