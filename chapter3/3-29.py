import requests
import re

def get_url(kiso_dict):
    url_file = kiso_dict['国旗画像'].replace(' ', '_')
    url = 'https://commons.wikimedia.org/w/api.php'
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url",
        "titles": f"File:{url_file}"
    }
    data = requests.get(url=url, params=params)
    return re.search(r'"url":"(.+?)"', data.text).group(1)

def remove_markup(target):
    #強調マークアップの除去
    r = re.compile(r"'{2,5}")
    target = r.sub("", target)
    #内部リンクの除去
    r = re.compile(r"\[\[(?:[^|]*?\|)??([^|]*?)\]\]")
    target = r.sub(r"\1", target)
    #外部リンクの除去
    r = re.compile(r"\[http:\/\/(?:[^\s]*?\s)?([^]]*?)\]")
    target = r.sub(r"\1", target)
    #htmlタグの除去
    r = re.compile(r"<\/?[br|ref][^>]*?>")
    target = r.sub("", target)
    return target

with open("uk.txt") as f:
    uk = f.read()

r = "\{\{基礎情報.*?\n(.*?)\}\}\n\n"
kiso = re.findall(r, uk, re.DOTALL)

r = "\|(.+?)\s=\s*(.+)"
kiso = re.findall(r, kiso[0])
kiso_dict = {}
for k, v in kiso:
    v = remove_markup(v)
    kiso_dict[k] = v

print(get_url(kiso_dict))