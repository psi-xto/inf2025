clA = [[],[]]
for s in open('27_A_17916.txt'):
    x,y = [float(i) for i in s.split()]
    if y < 8:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

clB = [[],[],[],[],[]]
for s in open('27_B_17916.txt'):
    x,y = [float(i) for i in s.split()]
    if y < 3 and x > 12: clB[0].append([x,y])
    elif x < 8 and y < 5: clB[1].append([x,y])
    elif 6 < y < 9: clB[2].append([x,y])
    elif 10 < y < 13: clB[3].append([x,y])
    else: clB[4].append([x,y])

def dist(k1,k2):
    x1,y1,x2,y2 = *k1,*k2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]

centerA = [center(i) for i in clA]
centerB = [center(i) for i in clB]

pxA = int(sum(x for x,y in centerA)/2*10000)
pyA = int(sum(y for x,y in centerA)/2*10000)
pxB = int(sum(x for x,y in centerB)/5*10000)
pyB = int(sum(y for x,y in centerB)/5*10000)

print(pxA, pyA)
print(pxB, pyB)