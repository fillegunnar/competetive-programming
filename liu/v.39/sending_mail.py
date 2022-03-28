N = int(input())

def dijkstras(n, m, s, t, nodes, i):
    distance = [float('inf') for _ in range(n)]
    distance[s] = 0
    prio_queue = [s]
    while True:
        if not prio_queue or m == 0:
            print("Case #" + str(i) + ": unreachable")
            break
        # Take out smallest distance in prio_queue
        min = float('inf')
        cn = None
        for node in prio_queue:
            if distance[node] < min:
                cn = node
                min = distance[node]
        prio_queue.remove(cn)
        # Check if we have arrived
        if cn == t:
            print("Case #" + str(i) + ": " + str(distance[cn]))
            break
        # Search through after neighbours
        for nb_w in nodes[cn]:
            if distance[cn] + nb_w[1] < distance[nb_w[0]]: 
                distance[nb_w[0]] = distance[cn] + nb_w[1]
                if nb_w[0] not in prio_queue:
                    prio_queue.append(nb_w[0])

for i in range(1, N+1):
    n, m, s, t = map(int, input().split(" "))
    nodes = {}
    for j in range(n): nodes[j] = []
    for j in range(m):
        n1, n2, w = map(int, input().split(" "))
        nodes[n1].append((n2, w))
        nodes[n2].append((n1, w))
    
    dijkstras(n, m, s, t, nodes, i)
    