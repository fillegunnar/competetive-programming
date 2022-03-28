import sys

seq = list(sys.stdin.read().split()) #Multiple lines, also splits on " "
n = int(seq[0])
seq = seq[1:]

weighted = [[1 for _ in range(n)] for __ in range(n)]

for i in range(n):
    if seq[i][0] == "*": weighted[i][0] = 0
    if seq[0][i] == "*": weighted[i][0] = 0

for i in range(1, n):
    for j in range(1, n):
        if seq[i][j] == "*":
            weighted[i][j] = 0
            continue
        weighted[i][j] = weighted[i-1][j]+weighted[i][j-1]

# print(weighted)
print(weighted[n-1][n-1]%(10**9+7))



# print(seq)