def f(x,y):
    if x > y or x == 6: return 0
    if x == y: return 1
    else: return f(x+2,y)+f(x*3,y)
print(f(1,25)*f(25,63))

def f(x,y):
    if x > y or x in [11,18]: return 0
    if x == y: return 1
    else: return f(x+1,y)+f(x*3,y)+f(x+2,y)
print(f(4,8)*f(8,23))

def f(x,y):
    if x > y or x == 43: return 0
    if x == y: return 1
    else: return f(x+2,y)+f(x+x-1,y)+f(x+x+1,y)
print(f(7,63))