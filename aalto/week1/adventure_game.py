move = ""
goal = ""
while True:
    possible_move = input()
    if (possible_move == "EW"):
        print("E", flush=True)
    elif possible_move == "W":
        move = "W"
        goal = "E"
    else:
        move = "E"
        goal = "W"
    if move != "":
        break

rooms = 1
read = move
while True:
    if read == goal:
        print(rooms, flush=True)
        break
    print(move)
    read = input()
    rooms += 1