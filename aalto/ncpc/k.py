import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n = seq[0]

knots = seq[1:n+1]
learned = seq[n+1:]

for i in knots:
    if i not in learned:
        print(i)
        break