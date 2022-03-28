
def add_node(n1, n2, nodes_dict):
    if n1 in nodes_dict.keys(): nodes_dict[n1].append(n2)
    else: nodes_dict[n1] = [n2]

    if n2 in nodes_dict.keys(): nodes_dict[n2].append(n1)
    else: nodes_dict[n2] = [n1]


def dfs(nodes_dict):
    print("DFS")
    stack = [1]
    discovered = []
    while stack:
        n = stack.pop()
        discovered.append(n)
        print(n, end=' ')
        for node in nodes_dict[n]:
            if node not in discovered:
                stack.append(node)
    print()
    
def bfs(nodes_dict):
    print("BFS")
    fifo = [1]
    discovered = []
    while fifo:
        n = fifo.pop(0)
        discovered.append(n)
        print(n, end=' ')
        for node in nodes_dict[n]:
            if node not in discovered:
                fifo.append(node)
    print()

def main(edges):
    nodes_dict = {}
    for edge in edges:
        n1 = edge[0]
        n2 = edge[1]
        add_node(n1, n2, nodes_dict)
    dfs(nodes_dict)
    bfs(nodes_dict)
    
edges = [
    (1, 2),
    (2, 5),
    (2, 6),
    (1, 3),
    (1, 4),
    (4, 7),
    (4, 8),
    (7, 9),
    (9, 10),
    (9, 11)
]
main(edges)