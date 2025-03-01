a = open('69932.txt').readline()
c = 0
m = 0
for i in range(0, len(a)-1):
    if a[i] in '0678' or (a[i-1] in '678' and a[i+1] in '678' and c!=0):
        c += 1
    else:
        m = max(m,c)
        c = 0
print(m)