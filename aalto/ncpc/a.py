import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, c = seq[0], seq[1]
seq = seq[2:]

bi = 0 
si = 0
print(0, end=" ")

for i in range(1, n):
    if (seq[i-1] - c) > (seq[bi] - c*(i-bi)):
        bi = i-1
    if (seq[i-1] + c) < (seq[si] + c*(i-si)):
        si = i-1
    alt1 = abs(seq[i] - seq[bi]) - c*(i-bi)
    alt2 = abs(seq[i] - seq[si]) - c*(i-si)
    if (alt1 < 0) and (alt2 < 0): print(0, end=" ")
    else: print(max(alt1, alt2), end=" ")
