import subprocess

url = "https://nlp100.github.io/data/popular-names.txt"
subprocess.run(["curl", "-O", url])

with open("popular-names.txt") as f:
    line_counts = len(f.readlines())

print(line_counts)