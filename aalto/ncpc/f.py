import sys
from math import factorial

n, k, p = map(float, sys.stdin.read().split())
c = factorial(n)/factorial(k)
print(n, k, p)
# print(1/(c*(p**k)))

nok = factorial(n)/(factorial(k)*factorial(n-k))

pr = nok * (p**k) * ((1-p)**(n-k))
print(pr)
print(1/(n*pr))
