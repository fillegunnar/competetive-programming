import sys
from queue import PriorityQueue

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, m, q = seq[0], seq[1], seq[2]
seq = seq[3:]

nodes = {}
for i in range(1, n+1): nodes[i] = {}
for i in range(0, m*3, 3):
    a, b, c = seq[i], seq[i+1], seq[i+2]
    nodes[a][b] = c
    nodes[b][a] = c

def djikstras(a, b):
    distance = [float('inf')] * (n+1)
    distance[a] = 0
    prio = [(0,a)]
    while True:
        # print(distance)
        if not prio: return -1
        # Take out smallest distance in prio_queue
        cn = prio.pop()[1]
        if cn == b: return distance[cn]
        # print(cn)
        changed = False
        for nb in nodes[cn]:
            if distance[cn] + nodes[cn][nb] < distance[nb]: 
                distance[nb] = distance[cn] + nodes[cn][nb]
                prio.append((distance[nb], nb))
                changed = True
        if changed: prio = sorted(prio, reverse=True)

for i in range(m*3, m*3+q*2, 2):
    a, b = seq[i], seq[i+1]
    print(djikstras(a, b))
