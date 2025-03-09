# не имеет значения начало конец
res = set()
def f(x,i):
    if i == 15:
        res.add(x)
    else:
        f(x*2,i+1)
        f(x*2+1,i+1)
f(1,0)
print(len(res))

res = set()
def f(x,i):
    if i == 8:
        if x in range(1000,1025):
            res.add(x)
    else:
        f(x+1,i+1)
        f(x+5,i+1)
        f(x*3,i+1)
f(1,0)
print(len(res))