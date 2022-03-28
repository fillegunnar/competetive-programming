def bfs(nodes_dict, moped, police, intersections):
    for i in range(intersections):
        if i not in nodes_dict.keys():
            print("-1")
            continue
        depth = 0
        fifo = [i]
        discovered = []
        escape = False
        while fifo:
            n = fifo.pop(0)
            discovered.append(n)
            for node in nodes_dict[n]:
                if node[0] not in discovered and node[1] >= moped:
                    if node[1] >= moped and node[1] < police:
                        escape = True
                        depth += 1
                        break
                    fifo.append(node[0])
            if escape: 
                print(depth)
                break
            depth += 1
        if not escape: print("-1")

def read():
    first = input().split(" ")
    intersections = int(first[0])
    roads = int(first[1])
    moped = int(first[2])
    police = int(first[3])
    nodes_dict = {}
    for i in range(roads):
        road = input().split(" ")
        n1 = int(road[0])
        n2 = int(road[1])
        width = int(road[2])
        if n1 in nodes_dict.keys(): nodes_dict[n1].append((n2, width))
        else: nodes_dict[n1] = [(n2, width)]

        if n2 in nodes_dict.keys(): nodes_dict[n2].append((n1, width))
        else: nodes_dict[n2] = [(n1, width)]
    return nodes_dict, moped, police, intersections



def main():
    nodes_dict, moped, police, intersections = read()
    bfs(nodes_dict, moped, police, intersections)
    
main()