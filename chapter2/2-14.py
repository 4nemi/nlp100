import sys

if len(sys.argv) != 2:
    print("Usage: python 2-14.py [number]")
    sys.exit(1)
with open("popular-names.txt") as f:
    for i, line in enumerate(f):
        if i < int(sys.argv[1]):
            print(line.rstrip())
        else:
            break
