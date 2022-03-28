import sys

seq = list(sys.stdin.read().split()) #Multiple lines, also splits on " "
n, m = int(seq[0]), int(seq[1])
seq = seq[2:]

index = {}

for i in range(n):
    for j in range(m-1, 0, -1):
        if seq[i][j] == '1': 
            index[1] = j
            break
        elif seq[i][j] == '2': 
            index[2] = j
            break
        elif seq[i][j] == '3': 
            index[3] = j
            break
        elif seq[i][j] == '4': 
            index[4] = j
            break
        elif seq[i][j] == '5': 
            index[5] = j
            break
        elif seq[i][j] == '6': 
            index[6] = j
            break
        elif seq[i][j] == '7': 
            index[7] = j
            break
        elif seq[i][j] == '8': 
            index[8] = j
            break
        elif seq[i][j] == '9': 
            index[9] = j
            break

for i in range(1, 10):
    cur_len = index[i]
    pos = 1
    two_eq = 0
    gone_through = []
    for j in range(1, 10):
        if i == j: continue
        elif cur_len < index[j]: 
            if index[j] not in gone_through:
                pos += 1
                gone_through.append(index[j])
    print(pos)
