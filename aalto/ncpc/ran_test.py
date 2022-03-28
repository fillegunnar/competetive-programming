import random

f = open("test.txt", "w")
n = random.randint(1, 10)
c = random.randint(1, 10)
f.write(str(n) + " " + str(c) + "\n")

for _ in range(n):
    f.write(str(random.randint(1,50)) + " ")
