string = input()
L = len(string)
Z = [0] * L

left = 0
right = 0
for i in range(1, L):
    if i > right:
        left = right = i
        while right < L and string[right] == string[right-left] and right-left < left:
            right += 1
        Z[i] = right - left
        right -= 1
    else:
        i1 = i - left
        if Z[i1] < (right - i + 1):
            Z[i] = Z[i1]
        else:
            left = i
            while right < L and string[right] == string[right-left]:
                right += 1
            Z[i] = right-left
            right -= 1

sp = ''
rep = 0
for i in range(L):
    if not sp and Z[i] == i:
        sp = string[:i]
        rep += 1
    if sp:
        bool1 = i % len(sp) == 0
        bool2 = Z[i] % len(sp) != 0
        bool3 = Z[i] != L-i
        if bool1 and (bool2 or (bool3 and not bool2)):
            print(i)
            sp = ''
if not sp:
    sp = string
print(sp)