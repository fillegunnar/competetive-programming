import sys

# n = int(input())
# seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
# seq = sys.stdin.read().split()
seq = []
for i in sys.stdin:
    # seq += i.split()
    seq += list(map(int, i.split()))
print(seq)