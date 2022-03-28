ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

w1 = input()
w2 = input()
w1 = list(w1)
w2 = list(w2)

output = []
while (True):
    changed_pos = []
    want_to_change = []
    output.append("".join(w1))
    if w1 == w2: break
    changed_previous = False
    for i in range(len(w1)):
        if changed_previous:
            changed_previous = False
            continue
        if w1[i] != w2[i]: #w2[i] ska vi byta till och w1[i] ska vi ta bort
            if (i == 0 or w1[i-1] != w2[i]) and \
                (i == len(w1)-1 or w1[i+1] != w2[i]):
                w1[i] = w2[i]
                changed_pos.append(i)
                changed_previous = True
            else:
                want_to_change.append(i)
    # May have changed some and may want to change more but to change to another letter first
    for i in want_to_change:
        if (i-1) in changed_pos or (i+1) in changed_pos:
            continue
        for letter in ALPHABET:
            if letter in w1 or letter in w2:
                continue
            w1[i] = letter
            changed_pos.append(i)
            break

for word in output:
    print(word)
    