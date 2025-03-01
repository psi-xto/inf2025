def div(h):
    divs = []
    for i in range(2, h+1,2):
        if h%i == 0:
            divs.append(i)
    return divs
for x in range(125256,125331):
    if len(div(x))==6:
        print(*div(x))
