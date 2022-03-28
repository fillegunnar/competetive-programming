possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

pw = ['A']
print(''.join(pw), flush=True)
read = input()
cur_pw = 0
cur_p = 0
while ('ACCESS GRANTED' not in read):
    # Find right length
    time = int(read.split('(')[1].split(' ')[0])
    if time == 5:
        pw.append('A')
        print(''.join(pw), flush=True)
        read = input()
        continue
    time -= 5 # remove first if and return
    # find right pw
    if cur_pw != time//9 - 1:
        cur_pw = time//9 - 1
        cur_p = 1
    else: cur_p += 1
    pw[cur_pw] = possible[cur_p]
    print(''.join(pw), flush=True)
    read = input()
