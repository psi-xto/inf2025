a = open('zadanie24_1.txt').readline()
c = 0
m = 0
for i in range(0, len(a)):
    if a[i]=='B': c+=1
    else:
        m = max(c, m)
        c = 0
print(m)