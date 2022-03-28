import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, m = seq[0], seq[1]
seq = seq[2:]

nodes = {}
for i in range(0, m*3, 3):
    a, b, c = seq[i], seq[i+1], seq[i+2]
    if a not in nodes.keys(): nodes[a] = []
    double = False
    for j in nodes[a]:
        if j[0] == b:
            if j[1] > c: j[1] = c
            double = True
    if not double: nodes[a].append([b, c])


print(nodes)
# print(seq)