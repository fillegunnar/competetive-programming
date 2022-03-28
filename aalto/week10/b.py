import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n = seq[0]
seq = seq[1:]

v_bottom = []
v_top = []
h_begins = []
h_ends = []

lines = {}

for i in range(0,n*4,4):
    x1, y1, x2, y2 = seq[i], seq[i+1], seq[i+2], seq[i+3]
    
    lines[(x1, y1)] = (x2,y2)

slines = list(sorted(lines.keys()))

for line in slines:
    if line[0] == lines[line][0]:
        v_bottom.append((line[0],line[1]))
        v_top.append((lines[line][0],lines[line][1]))
    else:
        h_begins.append((line[0],line[1]))
        h_ends.append((lines[line][0],lines[line][1]))

while h_ends:
    


