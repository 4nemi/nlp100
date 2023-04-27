import re
#MediaWikiの内部リンクマークアップの削除
def remove_innermarkup(target):
    r = re.compile(r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]')
    return r.sub(r'\1', target)

with open("uk.txt") as f:
    uk = f.read()

r = "\{\{基礎情報.*?\n(.*?)\}\}\n\n"
kiso = re.findall(r, uk, re.DOTALL)

r = "\|(.+?)\s=\s*(.+)"
kiso = re.findall(r, kiso[0])
kiso_dict = {}
for k, v in kiso:
    v = remove_innermarkup(v)
    kiso_dict[k] = v
#print(kiso_dict["国章リンク"])