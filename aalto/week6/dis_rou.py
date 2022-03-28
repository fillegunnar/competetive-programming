import sys
import queue

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, m = seq[0], seq[1]
seq = seq[2:]

capacity = {}
ports = {}
for a in range(1, n+1):
    capacity[a] = {}
    ports[a] = []

for i in range(0, m*2, 2):
    a, b = seq[i], seq[i+1]
    ports[a].append(b)
    if b not in capacity[a].keys(): 
        capacity[a][b] = 1
        capacity[b][a] = 0
    else: 
        capacity[a][b] = 1

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

def final_paths(flow):
    st = []
    st.append(1)
    pred = [None for _ in range(n+1)]
    paths = []
    while flow > 0:
        cn = st.pop()
        for nb in capacity[cn]:
            if pred[nb] == None and nb in ports[cn] and capacity[cn][nb] == 0:
                pred[nb] = cn
                if nb == n:
                    cn = n
                    path = []
                    while cn != 1:
                        path.append(cn)
                        cn = pred[cn]
                    path.append(1)
                    paths.append(path)
                    flow -= 1
                else: st.append(nb)
                pred[n] = None
    for path in paths:
        print(len(path))
        for i in range(len(path)-1, -1, -1):
            print(path[i], end=" ")
        print()
    
flow = 0
paths = []
while(True):
    pred = [None for _ in range(n+1)]
    pred[1] = 1
    bfs(pred)
    if pred[n] == None:
        print(flow)
        final_paths(flow)
        break
    df = 1
    cn = n
    while cn != 1:
        pr = pred[cn]
        capacity[pr][cn] -= df
        capacity[cn][pr] += df
        cn = pr
    flow += df
