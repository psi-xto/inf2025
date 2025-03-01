def f(x,a):
    if x <= 19:
        return a%2==0
    if a == 0:
        return False
    r = [f(x-1,a-1), f(x//3,a-1) if x%3==0 else f(x-2,a-1), f(x//5, a-1) if x%5==0 else f(x-3,a-1)]
    if a%2==0:
        return all(r)
    return any(r)
for i in range(20,100):
    if f(i,2):
        print(i)