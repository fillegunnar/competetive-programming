import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n = seq[0]
seq = seq[1:]



mini = seq[0]
tol = mini + seq[0]
for i in range(1,n):
    print(mini, tol)
    cur = seq[i]
    
    alt1, alt2 = 0, 0
    if tol >= cur: alt1 = mini
    else: alt1 = mini + (cur - tol)
        
    if cur >= seq[0]: alt2 = cur
    else: alt2 = seq[0] - cur
    
    if alt1 < alt2:
        if mini < alt1: tol += alt1-mini
        mini = alt1
        tol += cur
    else:
        mini = alt2
        tol = mini + alt2

print(mini)
    