import sys

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
dic = {}
for l in list(ALPHA):
    dic[l] = 0

seq = list(sys.stdin.read().split()) #Multiple lines, also splits on " "
n = int(seq[0])
s = list(seq[1])
m = len(s)
for l in s:
    dic[l] += 1

for l in list(ALPHA):
    
print(s)
ss = 0