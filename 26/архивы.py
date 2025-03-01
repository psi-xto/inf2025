a = open('26_demo.txt').readlines()
s,m = map(int,a[0].split())
a = sorted(int(i) for i in a[1:])
arc = []
for i in range(0, len(a)):
    if sum(arc)+a[i] > s: break
    arc.append(a[i])
print(len(arc), sum(arc))

# https://inf-ege.sdamgia.ru/problem?id=27423