from sys import _current_frames


temp = input().split(" ")
n = int(temp[0])
k = int(temp[1])

row = {}
ship_length = 1
for i in range(k):
    temp = input().split(" ")
    r = int(temp[0])
    c = int(temp[1])
    if r not in row.keys(): row[r] = [c,c]
    else: 
        if c < row[r][0]: row[r][0] = c
        elif c > row[r][1]: row[r][1] = c
        l = row[r][1] - row[r][0] + 1
        if l > ship_length: ship_length = l

possible_right = 0
possible_left = 0
cpos = float('inf')
for r in row.keys():
    if cpos == float('inf'): cpos = row[r][0]
    width_needed_on_row = row[r][1] - row[r][0]
    if 

# for i in range(1, n+1):

# print(min_width_needed)

# 11000
# 01000
# 00001
# 00001