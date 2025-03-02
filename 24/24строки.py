a = open('24_859.txt').readlines()
c = 0
for i in a:
    if i.count('S')==i.count('X'):
        c += 1
print(c)

a = open('24_587.txt').readlines()
c = 0
for i in a:
    if i.count('B')>=1.05*i.count('A'):
        c += 1
print(c)

a = open('24_2502.txt').readlines()
c = 0
for i in a:
    for x in range(0, len(i)-3):
        if i[x]+i[x+2]+i[x+3]=='KGE':
            c += 1
            break
print(c)