import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, c = seq[0], seq[1]
seq = seq[2:]

print(seq)