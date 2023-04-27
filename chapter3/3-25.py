import re
with open("uk.txt") as f:
    uk = f.read()

r = "\{\{基礎情報.*?\n(.*?)\}\}\n\n"
kiso = re.findall(r, uk, re.DOTALL)
r = "\|(.+?)\s=\s*(.+)"
kiso = re.findall(r, kiso[0])
print(kiso)