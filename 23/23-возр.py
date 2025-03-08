def f(x,y):
    if x > y: return 0
    if x == y: return 1
    else: return f(x+1,y)+f(x*2,y)

print(f(1,13))

def f(x,y):
    if x > y: return 0
    if x == y: return 1
    else: return f(x+1,y)+f(2*x,y)+f((2*x)+1,y)+f(10*x,y)
print(f(1,15))