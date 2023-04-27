import subprocess
import json

url = "https://nlp100.github.io/data/jawiki-country.json.gz"
subprocess.run(["curl", "-O", url])
subprocess.run(["gzip", "-d", "jawiki-country.json.gz"])
#jsonファイルを読み込み
with open("jawiki-country.json") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            uk = data["text"]
            break
with open("uk.txt", "w") as f:
    f.write(uk)