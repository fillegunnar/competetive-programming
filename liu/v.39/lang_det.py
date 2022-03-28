known = {"HELLO":"ENGLISH", "HOLA":"SPANISH", "HALLO":"GERMAN", "BONJOUR":"FRENCH", "CIAO":"ITALIAN", "ZDRAVSTVUJTE":"RUSSIAN"}

i = 1
while True:
    read = input()
    if read[-1] == "\r":
        read = read[:-1]
    if read == "#":
        break
    elif read in known.keys():
        print("Case " + str(i) + ": " + known[read])
    else:
        print("Case " + str(i) + ": UNKNOWN")
    i += 1
