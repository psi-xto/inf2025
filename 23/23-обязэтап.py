def f(x,y):
    if x > y: return 0
    if x == y: return 1
    else: return f(x+1,y)+f(x*2,y)+f(x+3,y)
print(f(3,9)*f(9,12)*f(12,20))

def f(x,y):
    if x < y: return 0
    if x == y: return 1
    else: return f(x-8,y)+f(x//2,y)
print(f(102,43)*f(43,5))