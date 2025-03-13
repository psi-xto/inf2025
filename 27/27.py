def dist(p1,p2):
    x1,x2,y1,y2 = *p1, *p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def center(kl): # на вход - кластер
    m = []
    for p in kl: # перебор точек кластера
        sm = sum(dist(p,p1) for p1 in kl) # сумма всех расстояний к другим точкам кластера
        m.append([sm,p]) # сумма расстояний, массив коорд точки
    return min(m) # точка центроид имеет наименьшую сумму

# обработка A
clA = [[],[]] # массив под 2 кластера
for s in open('27A.txt'):
    x,y = [float(i) for i in s.split()]
    if x<3:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

# обработка B
clB = [[],[],[]] # массив под 3 кластера
for s in open('27B.txt'):
    x,y = [float(i) for i in s.split()]
    if x > 4:
        clB[0].append([x,y])
    elif y >2.3:
        clB[1].append([x,y])
    else:
        clB[2].append([x,y])

print(len(clA[1]), len(clA)[2])
    
centerA = [center(kl) for kl in clA]
centerB = [center(kl) for kl in clB]
# смотрим только [1], сумму не надо

# считаем срарифм
sxA = sum(x for x,y in centerA)/2*10000 # колво кластеров
syA = sum(y for x,y in centerA)/2*10000
sxB = sum(x for x,y in centerB)/3*10000
syB = sum(y for x,y in centerB)/3*10000
