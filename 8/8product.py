from itertools import product
c = 0
for i in product('ABCWXYZ',repeat=6):
    s = ''.join(i)
    if  s[0] in 'WXYZ' and s[-1] in 'WXYZ' and all(s[i] not in 'WXYZ' for i in range(1,5)):
        c += 1
print(c)