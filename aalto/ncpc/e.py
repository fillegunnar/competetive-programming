import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, c = seq[0], seq[1]

for i in range(n):
    if i == 0:
        print(0, end=" ")
        continue
    a = abs(seq[i] - seq[i-1]) - c*abs(i-(i-1))
    print(a, end=" ")