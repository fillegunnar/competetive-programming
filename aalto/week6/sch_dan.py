import sys
import queue

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, m, k = seq[0], seq[1], seq[2]
seq = seq[3:]

capacity = {}
for a in range(n+m+2): capacity[a] = {}
for i in range(0, k*2, 2):
    a, b = seq[i], seq[i+1]
    capacity[a][b+n] = 1
    capacity[b+n][a] = 0

sink = n+m+1
for i in range(n+1, n+m+1):
    capacity[i][sink] = 1
    capacity[sink][i] = 0

source = 0
for i in range(1, n+1):
    capacity[source][i] = 1
    capacity[i][source] = 0

def bfs(pred):
    que = queue.Queue()
    que.put(source)
    while not que.empty():
        cn = que.get()
        for nb in capacity[cn]:
            if pred[nb] == None and capacity[cn][nb] > 0:
                pred[nb] = cn
                if nb == sink:
                    break
                que.put(nb)

def pairs():
    for i in range(1, n+1):
        for j in range(n+1, n+m+1):
            if j in capacity[i].keys() and capacity[i][j] == 0:
                print(i, j-n)

flow = 0
while(True):
    pred = [None for _ in range(n+m+2)]
    pred[source] = source
    bfs(pred)
    if pred[sink] == None: break

    df = float('inf')
    cn = sink
    while cn != source:
        pr = pred[cn]
        df = min(df, capacity[pr][cn])
        cn = pr
    cn = sink
    while cn != source:
        pr = pred[cn]
        capacity[pr][cn] -= df
        capacity[cn][pr] += df
        cn = pr
    flow += df

print(flow)
pairs()
