import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, q = seq[0], seq[1]
seq = seq[2:]

arr = seq[:n]
seq = seq[n:]

sum_arr = [0]*(n+1)
sum = 0
for i in range(1, n+1):
    sum += arr[i-1]
    sum_arr[i] = sum

for i in range(0, len(seq), 2):
    a, b = seq[i], seq[i+1]
    ans = sum_arr[b]-sum_arr[a-1]
    # print(sum_arr[a-1], sum_arr[b-1])
    print(ans)

# print(sum_arr)