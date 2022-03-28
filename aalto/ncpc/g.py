import sys
import math


seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n = seq[0]

covered = {}
for i in range(1, n*3, 3):
    x, y, r = seq[i], seq[i+1], seq[i+2]
    a = mathi.pi * r**2
    print(a)