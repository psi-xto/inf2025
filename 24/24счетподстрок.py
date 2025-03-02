s = open('24_314.txt').readline()
print(s.count('OCK') - s.count('STOCK'))

s = open('24_279.txt').readline()
# jboss и bossj вычитают jbossj дважды
print(s.count('BOSS') - s.count('JBOSS') - s.count('BOSSJ') + s.count('JBOSSJ'))

s = open('24_2498.txt').readline()
c = 0
for i in range(0, len(s)-2):
    if s[i]+s[i+1]+s[i+2] == 'XIX':
        c += 1
print(c)

s = open('24_2500.txt').readline()
c = 0
#поиск по паттерну G*ME
for i in range(0, len(s)-3):
    if s[i]+s[i+2]+s[i+3] == 'GME':
        c += 1
print(c)