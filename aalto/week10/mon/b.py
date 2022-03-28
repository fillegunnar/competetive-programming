import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, q = seq[0], seq[1]
seq = seq[2:]

arr = seq[:n]
seq = seq[n:]

mins = {}
for i in range(n):
    mins[i] = {}
    mins[i][i] = arr[i]

i = 1
while 2**i <= n:
    for j in range(n):
        jj = j + 2**i - 1 
        if jj < n:
            if j not in mins.keys():
                mins[j] = {}
            w = (jj-j+1)//2
            mins[j][jj] = min(mins[j][j+w-1], mins[j+w][jj])
        else:
            break
    i += 1
    
# print(mins)

for i in range(0, len(seq), 2):
    a, b = seq[i]-1, seq[i+1]-1
    # print(a,b)
    l = b-a+1
    k = 0
    while 2**k<=l: k += 1
    k -= 1
    k = 2**k
    # print(k)
    ans = min(mins[a][a+k-1], mins[b-k+1][b])
    print(ans)