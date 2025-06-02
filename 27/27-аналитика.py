def dist(p1,p2):
    x1,x2,y1,y2 = *p1, *p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def center(kl): 
    m = []
    for p in kl: 
        sm = sum(dist(p,p1) for p1 in kl)
        m.append([sm,p]) 
    return min(m) 

clA = [[],[]]
for s in open('27A.txt'):
    x,y = [float(i) for i in s.split()]
    if x<3:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

clB = [[],[],[]]
for s in open('27B.txt'):
    x,y = [float(i) for i in s.split()]
    if x > 4:
        clB[0].append([x,y])
    elif y >2.3:
        clB[1].append([x,y])
    else:
        clB[2].append([x,y])
    
centerA = [center(kl) for kl in clA]
centerB = [center(kl) for kl in clB]

sxA = sum(x for x,y in centerA)/2*10000
syA = sum(y for x,y in centerA)/2*10000
sxB = sum(x for x,y in centerB)/3*10000
syB = sum(y for x,y in centerB)/3*10000
