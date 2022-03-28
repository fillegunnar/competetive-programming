import sys

seq = list(sys.stdin.read().split()) #Multiple lines, also splits on " "
n = int(seq[0])
seq = seq[1:]

groups = {}
for i in range(0, n*3, 3):
    i, j, k = seq[i], seq[i+1], int(seq[i+2])
    if i not in groups.keys(): groups[i] = {}
    groups[i][j] = k

res = 0
possible = False
for g in groups:
    l, r = 0, 0
    if 'left' in groups[g]:
        l = groups[g]['left']
    if 'right' in groups[g]:
        r = groups[g]['right']
    res += max(l, r)
    
    if l == 0 and r == 0:
        res += 1
        
    if 'any' in groups[g] and groups[g]['any'] > 1: 
        possible = True
    
    if l != 0 and r != 0: possible = True
    

if possible: print(res+1)
else: print('impossible')