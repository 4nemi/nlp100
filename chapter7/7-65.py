#意味的アナロジーと文法的アナロジーの正解率を求めるプログラム

with open('questions-words-ans.txt') as f:
    semantic_correct = 0
    semantic_total = 0
    syntactic_correct = 0
    syntactic_total = 0
    for line in f:
        line = line.split()
        if line[0][:4] == 'gram':
            syntactic_total += 1
            if line[1] == line[2]:
                syntactic_correct += 1
        else:
            semantic_total += 1
            if line[1] == line[2]:
                semantic_correct += 1
    
    print('意味的アナロジー正解率: {} / {} = {}'.format(semantic_correct, semantic_total, semantic_correct/semantic_total))
    print('文法的アナロジー正解率: {} / {} = {}'.format(syntactic_correct, syntactic_total, syntactic_correct/syntactic_total))