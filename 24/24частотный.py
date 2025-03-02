a = open('24_2506.txt').readline().rstrip()
l = {x:a.count(x) for x in sorted(set(a))}
print(max(l.values()))

a = open('24_2509.txt').readline().rstrip()
l = {x:a.count(x) for x in sorted(set(a))}
print(max(l.values()) - min(l.values()))

a = open('24_2504.txt').readline().rstrip()
l = {x:0 for x in sorted(set(a))}
for i in range(0, len(a)-4):
    if a[i]+a[i+1]+a[i+3]+a[i+4]=='CBBC':
        l[a[i+2]] += 1
print(l)
print(max(l.values()))

a = open('24_2507.txt').readlines()
m = max(i.count('Q') for i in a)
for i in a:
    if i.count('Q') == m:
        l = {x:i.count(x) for x in sorted(set(i.rstrip()))}
        print(min(l.values()))
        print(l)
print(sum(i.count('C') for i in a))