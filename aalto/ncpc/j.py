import sys
import math

seq = list(map(int, sys.stdin.read().split()))

skari = [seq[0], seq[1]]
sola = [seq[2], seq[3]]
ekari = [seq[4], seq[5]]
eola = [seq[6], seq[7]]

# kommer alltid vara längst ifrån varandra i början eller slutet!?

sdist = math.sqrt((skari[0] - sola[0])**2 + (skari[1] - sola[1])**2)
edist = math.sqrt((ekari[0] - eola[0])**2 + (ekari[1] - eola[1])**2)
print(max(sdist, edist))
