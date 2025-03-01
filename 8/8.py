from itertools import permutations
c = 0
for i in permutations('ДЕЙКСТРА', r=6):
    s = ''.join(i)
    if s.count('Й')==1 and s.index("Й")!=5 and s[s.index("Й")+1] in 'ДКСТР':
        c += 1
print(c)