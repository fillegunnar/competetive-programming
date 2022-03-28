import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n = seq[0]
g = seq[1:n+1]
h = seq[n+1:n*2+1]

print(g,h)