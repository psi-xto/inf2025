a = open('24_2507.txt').readlines()
m = max(i.count('Q') for i in a)
for i in a:
    if i.count('Q') == m:
        l = {x:i.count(x) for x in sorted(set(i.rstrip()))}
        print(min(l.values()))
        print(l)
print(sum(i.count('C') for i in a))