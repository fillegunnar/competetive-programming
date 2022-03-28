n = int(input())
seq = input().split(" ")
prev = 0
moves = 0
for i in range(n):
    cur = int(seq[i])
    if cur < prev: 
        moves += prev - cur
        cur += prev - cur
    prev = cur

print(moves)


