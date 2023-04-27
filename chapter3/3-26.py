import re
#MediaWikiの強調マークアップの削除
def remove_stressmarkup(target):
    r = re.compile(r"'{2,5}")
    return r.sub("", target)

if __name__ == "__main__":
    with open("uk.txt") as f:
        uk = f.read()

    r = "\{\{基礎情報.*?\n(.*?)\}\}\n\n"
    kiso = re.findall(r, uk, re.DOTALL)

    r = "\|(.+?)\s=\s*(.+)"
    kiso = re.findall(r, kiso[0])
    kiso_dict = {}
    for k, v in kiso:
        kiso_dict[k] = remove_stressmarkup(v)
    #print(kiso_dict)