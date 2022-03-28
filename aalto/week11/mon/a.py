import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
x,y,r = seq[0],seq[1],seq[2]

tl = (x-r, y+r)
bl = (x-r, y-r)
br = (x+r, y-r)
tr = (x+r, y+r)


print(tl[0], tl[1])
print(bl[0], bl[1])
print(br[0], br[1])
print(tr[0], tr[1])