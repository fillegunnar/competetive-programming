n = int(input())

stacks = []
i = 1
while (n > 0):
    if n-i > i:
        stacks.append(i)
        n -= i
        i += 1
    else:
        stacks.append(n)
        n = 0

print(len(stacks))
for s in stacks: print(s, end=" ")
print()