from itertools import permutations
c = 0
for i in permutations('АБИКОЛУН', r = 8):
    s = ''.join(i)
    for x in 'ИОУ': s=s.replace(x,'А')
    for x in 'КЛН': s=s.replace(x,'Б')
    if 'АА' not in s and 'ББ' not in s:
        c += 1
print(c)

from itertools import permutations
c = 0
for i in permutations('01234567',r=5):
    s = ''.join(i)
    if s.count('1')==0 and s[0]!='0':
        for x in '3579': s=s.replace(x,'Н')
        for x in '02468': s=s.replace(x,'Ч')
        if 'ЧЧ' not in s and 'НН'not in s:
            c += 1
print(c)

from itertools import permutations
c = 0
for i in permutations('ДЕЙКСТРА', r=6):
    s = ''.join(i)
    if s.count('Й')==1 and s.index("Й")!=5 and s[s.index("Й")+1] in 'ДКСТР':
        c += 1
print(c)
