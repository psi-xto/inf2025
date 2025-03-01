def f(x,a,p0,p1):
    if x >= 21:
        return a%2==0
    if a == 0:
        return False
    r = []
    if p1!='+1': r += [f(x+1,a-1,'+1',p0)] # ластход свой
    if p1!='+2': r += [f(x+2,a-1,'+2',p0)]
    if p1!='*2': r += [f(x*2,a-1,'*2',p0)]
    if a%2==0:
        return all(r)
    return any(r)
for i in range(1,21):
    if not f(i,1,'','') and f(i,3,'',''):
        print(i)