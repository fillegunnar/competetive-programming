import sys

seq = list(map(int, sys.stdin.read().split())) #Multiple lines, also splits on " "
n, x = seq[0], seq[1]
seq = seq[2:]
prices = seq[:n]
pages = seq[n:]

maxs = [[0,0]] * n

for i in range(n):
    if i == 0:
        if prices[i] < x: maxs[i] = [prices[i], pages[i]]
        continue
    alt1 = 0
    alt2 = 0
    if maxs[i-1][0] + prices[i] < x:
        alt1 = maxs[i-1][1] + pages[i]
    if prices[i] < x: alt2 = pages[i]
    alt3 = maxs[i-1][1]
    if alt1>=alt2 and alt1>=alt3: 
        maxs[i] = [maxs[i-1][0]+prices[i], alt1]
    elif alt2>=alt1 and alt2>=alt3: 
        maxs[i] = [prices[i], alt2]
    else:
        maxs[i] = [maxs[i-1][0], alt3]
    print(maxs)
m = 0
for i in range(n):
    if maxs[i][1] > m: m = maxs[i][1]

print(m)

# for i in range(n):

# def rec_solve(i, cp, np):
#     if i == n: return 0
#     temp1 = np
#     if prices[i] + cp <= x:
#         temp1 = rec_solve(i+1, prices[i]+cp, pages[i]+np)
#     temp2 = rec_solve(i+1, cp, np)
#     return max(temp1, temp2)

# print(rec_solve(0, 0, 0))

# price_per_page = []
# for i in range(n):
#     price_per_page.append((prices[i]/pages[i], i))

# price_per_page = sorted(price_per_page)

# cc = 0
# n_pages = 0
# for i in range(n):
#     if cc + prices[price_per_page[i][1]] <= x:
#         cc += prices[price_per_page[i][1]]
#         n_pages += pages[price_per_page[i][1]]

# print(n_pages)
