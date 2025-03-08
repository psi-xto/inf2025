f = open('26_838.txt')
n = f.readline()
a = sorted([int(i) for i in f.readlines()])
d1 = []
d2 = []
while len(a)!=0:
    d1 += [a[-1]]
    a.pop(-1)
    while sum(d2)<=sum(d1):
        d2 += [a[0]]
        a.pop(0)
print(len(d1),len(d2))
