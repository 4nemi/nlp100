import sys

def split_file(N):
    with open("popular-names.txt") as f:
        lines = f.readlines()
        line_counts = len(lines)
        if N > line_counts:
            print("N is larger than the number of lines in the file.")
            sys.exit(1)
        split_n = line_counts // N
        for i in range(N):
            with open(f"popular-names-{i}.txt", "w") as g:
                if i == N - 1:
                    for line in lines[i*split_n:]:
                        g.write(line)
                else:
                    for line in lines[i*split_n:(i+1)*split_n]:
                        g.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2-16.py [number]")
        sys.exit(1)

    split_file(int(sys.argv[1]))