import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n = seq[0]
seq = seq[1:]

skills = []
for i in range(0, n*2, 2):
    b,p = seq[i],seq[i+1]

    skills.append((b, p))

skills = sorted(skills)

possible = True
possible_sum = (skills[0][0]+skills[n-1][0], skills[0][1]+skills[n-1][1])
for i in range(1, n//2):
    cur_sum = (skills[i][0]+skills[n-i-1][0], skills[i][1]+skills[n-i-1][1])
    if cur_sum != possible_sum:
        possible = False
        break

if n%2 == 0 and possible: print("possible")
else: print("impossible")