from sys import setrecursionlimit
def F(n):
    if n == 1: return 5
    if n == 2: return 5
    else: return 5*F(n-1)-4*F(n-2)

setrecursionlimit(9999)
print(F(13))