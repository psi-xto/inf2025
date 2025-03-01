s = open('24valid.txt').readline()
for c in '23456': s = s.replace(c,'1')
s = s.replace('*','-')
for c in 'CD': s = s.replace(c,'B')
s = s.replace('B', ' ')
while '--' in s: s = s.replace('--', '- -')
while 'AA' in s: s = s.replace('AA', 'A A')
s = s.replace('1A','1 A').replace('-A','- A')

s = sorted(s.split(), key=len, reverse=1)

for c in s:
    if c[0]=='A':
        print(c, len(c))
        input()
# валидность руками
