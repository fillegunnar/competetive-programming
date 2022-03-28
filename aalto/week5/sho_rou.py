import sys
from queue import PriorityQueue

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, m = seq[0], seq[1]
seq = seq[2:]

nodes = {}
for i in range(1, n+1): nodes[i] = {}
for i in range(0, m*3, 3):
    a, b, c = seq[i], seq[i+1], seq[i+2]
    if b in nodes[a].keys() and nodes[a][b] < c: 
        continue
    nodes[a][b] = c
    
    

distance = [float('inf')] * (n+1)
distance[1] = 0
prio = {}
for i in range(1, n+1): prio[i] = distance[i]
while True:
    if not prio: break
    # Take out smallest distance in prio_queue
    s = sorted(prio)
    cn = s[0]
    prio.pop(cn)
    print(cn)
    for nb in nodes[cn]:
        if distance[cn] + nodes[cn][nb] < distance[nb]: 
            distance[nb] = distance[cn] + nodes[cn][nb]
            prio[nb] = distance[nb]


for i in range(1, len(distance)):
    print(distance[i], end=" ")
# print(seq)