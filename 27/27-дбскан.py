from math import dist

data = []
cls = []
for s in open("27b.txt").readlines():
    x, y = [float(i) for i in s.split()]
    data.append([x, y])

while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p, p1) < 2.9]
        for p1 in sosed:
            cl.append(p1)
            data.remove(p1)
    cls.append(cl)
print([len(s) for s in cls])


def centroid(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]


centers = [centroid(cl) for cl in cls]

px = abs(int(sum(x for x, y in centers) / 3 * 10000))
py = abs(int(sum(y for x, y in centers) / 3 * 10000))

print(px, py)


i = open("27b.txt").readlines()
from math import dist

data = []
for j in i:
    x, y = map(float, j.split())
    data.append([x, y])
cls = []
while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p, p1) <= 1]
        for p1 in sosed:
            data.remove(p1)
            cl.append(p1)
    cls.append(cl)
cls = [cl for cl in cls if len(cl) > 5]
print([len(cl) for cl in cls])


def centroid(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]


center = [centroid(cl) for cl in cls]

px = int(sum(x for x, y in center) / 5 * 10000)
py = int(sum(y for x, y in center) / 5 * 10000)
print(px, py)
