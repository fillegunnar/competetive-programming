import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n = seq[0]
seq = seq[1:]

def start_grid(pos):
    sg = [0] * n
    for c in pos:
        if pos[c] < 0 or pos[c] >= n: return [-1]
        if sg[pos[c]] != 0: return [-1]
        sg[pos[c]] = c
    return sg


while(n!=0):
    pos = {}
    for i in range(0, n*2, 2):
        c, p = seq[i], seq[i+1]
        pos[c] = i//2 + p

    sg = start_grid(pos)
    for i in sg: print(i, end=" ") 

    # next case
    temp = seq[n*2]
    seq = seq[n*2+1:]
    n = temp
    if n != 0: print()
