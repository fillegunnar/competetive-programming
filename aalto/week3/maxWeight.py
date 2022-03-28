g = [4, 1, 1, 1, 4, 5, 6]
heaviest = []

for i in range(len(g)):
    if i == 0: 
        heaviest.append([g[i], [], 0, []])
        continue
    value1 = heaviest[i-1][0]
    index1 = heaviest[i-1][1]
    value2 = heaviest[i-1][2]
    index2 = heaviest[i-1][3]

    heaviest_selected = value2 + g[i]
    temp = value1-g[i-1]+g[i]
    if temp > heaviest_selected: 
        heaviest_selected = temp
    heaviest.append([heaviest_selected, [], value1, []])

print(max(heaviest[-1][0], heaviest[-1][2]))

min_vertex = []

for i in range(len(g)):
    if i == 0:
        min_vertex.append([g[i], 0])
        continue
    prev_selected = min_vertex[i-1][0]
    prev_not_selected = min_vertex[i-1][1] + g[i] # Does not always have to be the case that the previous was not selected
    temp = prev_selected+g[i]
    if temp < prev_not_selected: prev_not_selected = temp
    min_vertex.append([prev_not_selected, prev_selected])

print(min(min_vertex[-1][0], min_vertex[-1][1]))



