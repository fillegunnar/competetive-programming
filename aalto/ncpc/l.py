import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
k = seq[0]

obs = seq[1:]

next_time = float('inf')
for i in range(0, len(obs), 3):
    y = obs[i]
    c1 = obs[i+1]
    c2 = obs[i+2]
    
    small = 0
    gcd = 0
    if c1 > c2: small = c2
    else: small = c1
    for i in range(small+1, 0, -1):
        if (c1 % i == 0) and (c2 % i == 0): 
            gcd = i
            break
    
    next = y + (c1*c2)/gcd
    if next < next_time:
        next_time = int(next)

print(next_time)

