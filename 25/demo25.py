def div(h):
    divs = set()
    for i in range(2, int(h**0.5) + 1):
        if h % i == 0:
            divs.add(i)
            divs.add(h // i)
    return sorted(divs)


for i in range(800001, 1000001):
    a = div(i)
    if len(a) > 1:
        if (max(a) + min(a)) % 10 == 4:
            print(i, max(a) + min(a))
