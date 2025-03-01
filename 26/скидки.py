l = [int(i) for i in open('inf_22_10_20_26.txt').readlines()]
n = l[0]
del(l[0])
l.sort()
res = []
m = 0
while l[0] <= 50:
    res += [l[0]]
    del(l[0])
for i in range(0, len(l)):
    if i < len(l)//2:
        res += [l[i]*0.75]
        m = max(m, l[i])
    else: 
        res += [l[i]]
print(round(sum(res)), m)

# https://inf-ege.sdamgia.ru/problem?id=29674