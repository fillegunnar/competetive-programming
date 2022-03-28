def bfs(map, start, h, w):
    fifo = [[start[0], start[1], ""]]
    discovered = []
    found = False
    res = []
    while fifo:
        cur_pos = fifo.pop(0)
        discovered.append([cur_pos[0], cur_pos[1]])
        possible_moves = []
        possible_moves.append([cur_pos[0], cur_pos[1]-1, cur_pos[2]])
        possible_moves.append([cur_pos[0], cur_pos[1]+1, cur_pos[2]])
        possible_moves.append([cur_pos[0]-1, cur_pos[1], cur_pos[2]])
        possible_moves.append([cur_pos[0]+1, cur_pos[1], cur_pos[2]])
        for i in range(4):
            r = possible_moves[i][0]
            c = possible_moves[i][1]
            if [r, c] in discovered or r>h-1 or r<0 or c>w-1 or c<0: continue
            elif map[r][c] == "#": continue
            else: 
                path = possible_moves[i][2]
                if i == 0: path += "L"
                elif i == 1: path += "R"
                elif i == 2: path += "U"
                elif i == 3: path += "D"
                fifo.append([r, c, path])
            if map[r][c] == "B": 
                found = True
                res = fifo[-1]
                break
        if found: break
    if found:
        print("YES")
        print(len(res[2]))
        print(res[2])
    else:
        print("NO")

temp = input().split(" ")
h = int(temp[0])
w = int(temp[1])

map = []
start = []

for i in range(h):
    line = input()
    if line[-1] == "\r": line = line[:-1]
    if "A" in line: start = [i, line.find("A")]
    map.append(line)
if start == []: print("NO")
else: bfs(map, start, h, w)
