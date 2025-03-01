a = open('24_10105.txt').readline().split('T')
print(a)
m = 0
for i in range(0, len(a)-100):
    r = 'T'.join(a[i:i+100+1])
    m = max(len(r), m)
print(m)