def f(x,a):
    if x >= 36:
        return a%2==0
    if a == 0:
        return False
    r = [f(x+1,a-1),f(x+2,a-1),f(x*2,a-1)]
    if a%2==0:
        return any(r)
    return any(r)
for i in range(1,36):
    if f(i,2):
        print(i)