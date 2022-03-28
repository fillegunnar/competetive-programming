import sys
import copy

seq = list(sys.stdin.read().split()) #Multiple lines, also splits on " "
n, m, string = int(seq[0]), int(seq[1]), seq[2]
string = [''] + list(string) # add '' to index right
ops = seq[3:]

for i in range(0,m*3,3):
    op = int(ops[i])
    if op == 1:
        k, x = int(ops[i+1]), ops[i+2]
        string[k] = x
    else: 
        a, b = int(ops[i+1]), int(ops[i+2])
        p = string[a:b+1]
        p2 = copy.copy(p)
        p2.reverse()
        if p == p2:
            print("YES")
        else: 
            print("NO")