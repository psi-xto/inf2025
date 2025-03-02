from itertools import product
c = 0
m = 0
for i in product('АИМРЯ', repeat=4):
    c += 1
    i = ''.join(i)
    if c == 211:
        print(i)
        break