n = int(input())
dreams = []

for _ in range(n):
    querie = input()
    if querie[-1] == "\r": querie = querie[:-1]
    if querie == "Kick":
        if dreams: dreams.pop()
    elif querie == "Test": 
        if dreams: print(dreams[-1])
        else: print("Not in a dream")
    else:
        dreams.append(querie.split(" ")[1])
