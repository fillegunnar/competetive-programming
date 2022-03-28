n = int(input())
seq = list(map(int, input().split()))

dic = {}
for i in range(n):
    if seq[i] not in dic.keys(): dic[seq[i]] = []
    dic[seq[i]].append(i+1)

stack = [list(dic.keys())[0]]
discovered = []
keys_left = list(dic.keys())
cycles = 0

while True:
    if not stack:
        if not keys_left:
            break
        stack.append(keys_left[0])
    n = stack.pop()
    discovered.append(n)
    if n not in keys_left: continue
    keys_left.remove(n)
    # print(n, end=' ')
    for node in dic[n]:
        if node not in discovered:
            stack.append(node)
            continue
        cycles += 1

print(cycles)
