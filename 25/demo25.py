def div(h):
    divs = []
    for i in range(2,h//2+1):
        if h%i==0:
            divs.append(h//i)
    return sorted(divs)
for i in range(800001, 1000001):
    a = div(i)
    if len(a)>1:
        if (max(a)+min(a))%10 == 4:
            print(i, max(a)+min(a))