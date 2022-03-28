temp = input()
pattern = input()
string = pattern + ":" + temp
L = len(string)
z_array = [0] * L

left = 0
right = 0
count = 0
for i in range(1, L):
    if i > right:
        left = right = i
        while right < L and string[right] == string[right-left]:
            right += 1
        z_array[i] = right - left
        right -= 1
    else:
        i1 = i - left
        if z_array[i1] < (right - i + 1):
            z_array[i] = z_array[i1]
        else:
            left = i
            while right < L and string[right] == string[right-left]:
                right += 1
            z_array[i] = right-left
            right -= 1

for i in z_array:
    if i == len(pattern): count += 1
print(count)