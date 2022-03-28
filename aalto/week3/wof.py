n = int(input())
seq = list(map(int, input().split()))

def init(start_color):
    value = [[0,0,0] for _ in range(n)]
    ready = [[False, False, False] for _ in range(n)]

    def compute(i, color):
        if color == 'b':
            if ready[i][0]:
                print("hej")
                pass
            value[i][0] = solve(i, color)
            ready[i][0] = True
        elif color == 'r':
            if ready[i][1]:
                print("hej")
                pass
            value[i][1] = solve(i, color)
            ready[i][1] = True
        elif color == 'g':
            if ready[i][2]:
                print("hej")
                pass
            value[i][2] = solve(i, color)
            ready[i][2] = True

    
    def solve(i, color):
        if i == n-1:
            if start_color == color:
                return -float('inf')
            if color == 'b':
                return seq[i]
            if color == 'r':
                return -seq[i]
            if color == 'g':
                return 0
        
        if color == 'b':
            compute(i+1, 'r')
            compute(i+1, 'g')
            return max(value[i+1][1], value[i+1][2]) + seq[i]
        if color == 'r':
            compute(i+1, 'b')
            compute(i+1, 'g')
            return max(value[i+1][0], value[i+1][2]) - seq[i]
        if color == 'g':
            compute(i+1, 'b')
            compute(i+1, 'r')
            return max(value[i+1][0], value[i+1][1])

    return solve(0, start_color)

print(max(init('b'), init('r'), init('g')))


# import sys
 
# n = int(input())
# cs = list(map(int, input().split()))
 
# def init(heighs, start_color):
#     sys.setrecursionlimit(max(n*5, 1000))
#     value = [[0, 0, 0] for _ in range(n)]
#     ready = [[False, False, False] for _ in range(n)]
    
#     def compute(k, color):
#         if color == 'black':
#             if not ready[k][0]:
#                 value[k][0] = solve(k, color)
#                 ready[k][0] = True
#         if color == 'green':
#             if not ready[k][1]:
#                 value[k][1] = solve(k, color)
#                 ready[k][1] = True
#         if color == 'red':
#             if not ready[k][2]:
#                 value[k][2] = solve(k, color)
#                 ready[k][2] = True
 
#     def solve(k, color):
#         # return the best solution for the k:-1 long path
#         if k == n-1:
#             if start_color == color:
#                 return -10**6
#             else:
#                 if color == 'black':
#                     return heighs[k]
#                 elif color == 'red':
#                     return - heighs[k]
#                 else:
#                     return 0
 
#         if color == 'black':
#             compute(k+1, 'green')
#             compute(k+1, 'red')
#             return max(value[k+1][1], value[k+1][2]) + heighs[k]
#         elif color == 'green':
#             compute(k+1, 'red')
#             compute(k+1, 'black')
#             return max(value[k+1][0], value[k+1][2])
#         elif color == 'red':
#             compute(k+1, 'green')
#             compute(k+1, 'black')
#             return max(value[k+1][0], value[k+1][1]) - heighs[k]
    
#     return solve(0, start_color)
 
# print(max(init(cs, 'black'), init(cs, 'green'), init(cs, 'red')))




# n = int(input())
# seq = input().split(" ")
# maxm = []
# maxi = []
# minm = []
# mini = []
# div = n/3

# for i in range(n):
#     seq[i] = int(seq[i])

# maxb = []
# prev_c = "n"
# for i in range(n):
#     if i == 0:
#         maxb.append([cur, div-1, div, div])
#         prev_c = "b"
#     match prev_c:
#         case 'b':

#         case _:
#             pass
#     cur = seq[i]
#     prev = seq[i-1]


# for i in range(n):
#     cur = int(seq[i])
#     if len(maxm) < div:
#         maxm.append((cur, i))
#         minm.append((cur, i))
#         continue
#     if cur > max()

# def color(seq, prev, win, i):
#     if i == n:
#         return win
#     elif prev == "n":
#         print(max(color(seq, "b", win+int(seq[i]), i+1), color(seq, "r", win-int(seq[i]), i+1), color(seq, "g", win, i+1)))
#     elif prev == "b":
#         return max(color(seq, "g", win, i+1), color(seq, "r", win-int(seq[i]), i+1))
#     elif prev == "r":
#         return max(color(seq, "g", win, i+1), color(seq, "b", win+int(seq[i]), i+1))
#     else:
#         return max(color(seq, "b", win+int(seq[i]), i+1), color(seq, "r", win-int(seq[i]), i+1))

# color(seq, "n", 0, 0)
    

# for i in range(n):
#     cur = int(seq[i])
#     if i == 0:
#         maxm.append([cur, div-1, div, div], [-cur, div, div-1, div], [0, div, div, div-1])
#         continue
#     prev = maxm[-1]
#     # next black
#     if prev[1][0] > prev[2][0] and prev[1][1] > 0:
#         next_black = [prev[0][0]+prev[1][0], prev[1][1]-1, prev[1][2], prev[1][2]]
#         if next_black[0] > cur
#     if i == 1:
#         if prev > seq[i]: maxm.append([prev, div-1, div, div-1])
#         else: maxm.append([cur, div-1, div, div-1])
#         continue
