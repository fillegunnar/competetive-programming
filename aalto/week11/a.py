import sys

seq = list(sys.stdin.read().split()) #Multiple lines, also splits on " "
n, k = int(seq[0]), int(seq[1])
seq = seq[2:]

events = {}
for i in range(0, n*2, 2):
    name, s = seq[i], int(seq[i+1])
    events[name] = [s, 0, 0] # (value now, number of times event occurs, threshold)

l = int(seq[n*2])
seq = seq[n*2+1:]


possible = True
for i in range(0, l*2, 2):
    e, t = seq[i], int(seq[i+1])
    if t > events[e][0]:
        diff = t - events[e][0]
        if diff > k:
            possible = False
            break
        k -= diff
        events[e][0] = t
    events[e][1] += 1
    if t > events[e][2]: events[e][2] = t

score = 0
potential = {}
if possible:
    for e in events:
        v, x, t = events[e][0], events[e][1], events[e][2]
        p = 0
        if v == t: p = (v+1)*x
        else: p = x
        i = 0
        potential[e] = p
    
    potential = dict(sorted(potential.items(), key=lambda item: item[1]))
    
    while k>0:
        k -= 1
        e = list(potential.keys())[-1]
        score += potential[e]
        events[e][0] += 1 
        v, x, t = events[e][0], events[e][1], events[e][2]
        p = 0
        if v == t: p = (v+1)*x
        else: p = x
        i = 0   
        if p != potential[e]:
            potential[e] = p
            potential = dict(sorted(potential.items(), key=lambda item: item[1]))

print(score)