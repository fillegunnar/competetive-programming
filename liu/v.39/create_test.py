import random

f = open("t2.txt", "w")
f.write("1\n")
f.write("20000 50000 0 50000\n")

for i in range(2000):
    for j in range(i+1, 2000):
        n = random.randint(0, 100000)
        f.write(str(i)+" "+str(j)+" "+str(n)+"\n")
