from itertools import product
c = 0
for i in product('ЕЛМРУ', repeat=4):
    c += 1
    if i[0]=="Л":
        print(c)
        break

from itertools import product
c = 0
m = 0
for i in product('АГИЛМОРТ', repeat=4):
    c += 1
    i = ''.join(i)
    if i[2]+i[3]=="ИМ":
        m = max(c,m)
print(m)

from itertools import product
c = 0
m = 0
for i in product('АИМРЯ', repeat=4):
    c += 1
    i = ''.join(i)
    if c == 211:
        print(i)
        break