def f(x,y,a):
    if x+y >= 81:
        return a%2==0
    if a == 0:
        return False
    v = [f(x+1,y,a-1),f(x*2,y,a-1),f(x,y+1,a-1),f(x,y*2,a-1)]
    if a%2==0:
        return all(v)
    return any(v)
for i in range(1,74):
    if not f(7,i,2) and f(7,i,4):
        print(i)
