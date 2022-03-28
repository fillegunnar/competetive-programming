a, b = map(int, input().split())

months = 0
pairs = 1
mating = 0
newborn = 0
for i in range(1, 1000+1):
    pairs += mating
    if pairs >= a: 
        if pairs > b:
            break
        months += 1
    if i % 2 == 0:
        newborn += 1
        mating += newborn
print(months)