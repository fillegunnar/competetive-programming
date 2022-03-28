
def read():
    col = int(input())
    heights = input()
    heights = heights.split(" ")
    return col, heights

def main():
    col, heights = read()
    water = 0
    temp = []
    last_big = 0
    for i in range(col):
        cur = int(heights[i])
        temp.append([cur, last_big])
        if cur > last_big: 
            last_big = cur
        
    last_big = 0
    for i in range(col-1, -1, -1):
        cur = int(heights[i])
        temp2 = temp[i]
        if temp2[1] > last_big:
            temp2[1] = last_big
        water += max(temp2[0], temp2[1])
        if cur > last_big:
            last_big = cur
    print(water)

main()