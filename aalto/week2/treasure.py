temp = input().split(" ")
n = int(temp[0])
k = int(temp[1])

row = {}
width_needed = 1
for i in range(k):
    temp = input().split(" ")
    r = int(temp[0])
    c = int(temp[1])
    if r not in row.keys(): row[r] = [c,c]
    else: 
        if c < row[r][0]: row[r][0] = c
        elif c > row[r][1]: row[r][1] = c
        l = row[r][1] - row[r][0] + 1
        if l > width_needed: width_needed = l

print(width_needed)

# 1100
# 0111
# 0100
# 1110