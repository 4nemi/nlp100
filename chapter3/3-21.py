import re
with open("uk.txt") as f:
    lines = f.readlines()
# 正規表現を使って抽出
pattern = r"\[\[Category:(.*?)(?:\|.*)?\]\]"
for line in lines:
    category = re.search(pattern, line)
    if category:
        print(category.group(0))