a = open('24_4113.txt').readline().rstrip()
b = [0]*len(a)
for i in range(0, len(a)-1):
    if a[i]+a[i+1]=='BB' or a[i]+a[i+1]=='DD':
        b[i+1]=b[i-1]+1
print(max(b))

l = open('24_4546.txt').readline()
x = [0]*len(l)
for i in range(0, len(l)-2):
    if l[i]+l[i+2] == 'AA' or l[i]+l[i+2] == 'CC':
        x[i+3]=x[i]+1
print(max(x))