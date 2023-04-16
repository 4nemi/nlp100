import sys

if len(sys.argv) != 2:
    print("Usage: python 2-15.py [number]")
    sys.exit(1)
with open("popular-names.txt") as f:
    lines = f.readlines()
    for i in reversed(range(int(sys.argv[1]))):
        print(lines[-1-i].rstrip())