import re
with open("uk.txt") as f:
    uk = f.read()
# 正規表現を使って抽出
pattern = r"\[\[Category:(.*?)(?:\|.*)?\]\]"
category = re.findall(pattern, uk)
for c in category:
    print(c)