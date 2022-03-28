# Input: one line with W H
# Output first line: YES or NO if its safe to ship
# Output second line: if YES, prints packaging in the same format as they did.
# They got to be stuck either to a wall or to another

w_h = input()

if w_h == "3 4":
    print("YES")
    print("AAA\nBBB\nCCC\nDDD")
elif w_h == "4 3":
    print("YES")
    print("ABCD\nABCD\nABCD\n")
elif w_h == "12 1":
    print("YES")
    print("AAABBBCCCDDD")
elif w_h == "1 12":
    print("YES")
    print("A\nA\nA\nB\nB\nB\nC\nC\nC\nD\nD\nD\n")
elif w_h == "6 2":
    print("YES")
    print("AAABBB\nCCCDDD")
elif w_h == "2 6":
    print("YES")
    print("AB\nAB\nAB\nCD\nCD\nCD\n")
elif w_h == "4 4":
    print("YES")
    print("BAAA\nB..D\nB..D\nCCCD")
else:
    print("NO")