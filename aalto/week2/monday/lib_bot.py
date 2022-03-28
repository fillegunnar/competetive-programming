# n buildings with n floors with n aisles with
# n bookshelves with n books
# print("E", flush=True)

def bin_search(begin, end, search_for, n):
    per_shelf = n
    per_aisle = n**2
    per_floor = n**3
    per_building = n**4
    index = [0,0,0,0,0]

    while (True):
        middle = begin + (end-begin)//2
        for i in range(4, 0, -1):
            temp = middle//n**i
            middle -= temp * n**i
            index[-i] = temp+1
        building = (middle//per_building)
        middle -= per_building*building
        floor = (middle//per_floor)+1
        middle -= per_floor
        aisle = (middle//per_aisle)+1
        middle -= per_aisle
        shelf = (middle//per_shelf)+1
        middle -= per_shelf
        book = middl, flush=e
        print("FETCH"+" "+building+"."+floor+"."+aisle+"."+shelf+"."+book, flush=True)
        
        found = input().split(" ")[1]
        if (found == search_for or middle == end or middle == begin): break
        elif (found < search_for): begin = middle
        else: end = middle

while True:
    n = int(input().split(" ")[1])
    search_for = input().split(" ")[1]
    begin = 0
    end = n**5
    bin_search(begin, end, search_for, n)
    
    # bin_search(begin, end, search_for)


