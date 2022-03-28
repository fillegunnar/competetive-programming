import sys
import queue

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, m = seq[0], seq[1]
seq = seq[2:]

capacity = {}
for a in range(1, n+1):
    capacity[a] = {}

for i in range(0, m*2, 2):
    a, b = seq[i], seq[i+1]
    capacity[a][b] = 1
    capacity[b][a] = 1

def bfs(pred):
    que = queue.Queue()
    que.put(1)
    while not que.empty():
        cn = que.get()
        for nb in capacity[cn]:
            if pred[nb] == None and capacity[cn][nb] > 0:
                pred[nb] = cn
                if nb == n:
                    break
                que.put(nb)

def min_cut(pred):
    # print(pred)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if pred[i] != None and pred[j] == None \
                and (j in capacity[i].keys()):
                print(i, j)

flow = 0
while(True):
    pred = [None for _ in range(n+1)]
    pred[1] = 1
    bfs(pred)
    if pred[n] == None:
        print(flow)
        min_cut(pred)
        break
    df = float('inf')
    cn = n
    while cn != 1:
        pr = pred[cn]
        df = min(df, capacity[pr][cn])
        cn = pr
    cn = n
    while cn != 1:
        pr = pred[cn]
        capacity[pr][cn] -= df
        capacity[cn][pr] += df
        cn = pr
    flow += df
