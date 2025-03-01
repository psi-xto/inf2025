l = [int(i) for i in open('17.txt')]
c = 0
m = 0
mini = min(i for i in l if abs(i)%10==7)
for i in range(0, len(l)-1):
    if abs(l[i])%10==abs(l[i+1])%10:
        if (abs(l[i])%7==0 and abs(l[i+1])%7!=0) or (abs(l[i])%7!=0 and abs(l[i+1])%7==0):
            if l[i]**2+l[i+1]**2 <= mini**2:
                    c += 1
                    m = max(m, l[i]**2+l[i+1]**2)
print(c, m)