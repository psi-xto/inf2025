data = []
for s in open("27a.txt"):
    x, y = [float(z) for z in s.split()]
    data.append([x, y])

from math import dist

cls = []
m = 2  # дельта для дбскана

while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p, p1) < m]
        cl = cl + sosed
        for p1 in sosed:
            cl.append(p1)
            data.remove(p1)
    cls.append(cl)


# для аномалий:
# cls = [cl for cl in cls if len(cl)>10]


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centroid = [center(i) for i in cls]

sx = sum(x for x, y in centroid) / 2 * 10000
sy = sum(y for x, y in centroid) / 2 * 10000
