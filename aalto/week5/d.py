xtest = list(map(int, input().split()))

x1 = xtest[0]
x2 = xtest[1]

for x in range(xtest[2]-2):
    y = x2
    x2 += x1
    x1 = y

print(x2)