import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n = seq[0]
seq = seq[1:]

for i in range(0, n*4, 4):
    x1, y1, x2, y2 = seq[i], seq[i+1], seq[i+2], seq[i+3]
    

print(seq)