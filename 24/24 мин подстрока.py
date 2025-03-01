i = open('24_9169.txt').readline()
l = k = 0
m = 999999999
i = i.replace('FAT','BAD')
for r in range(2,len(i)):
    if i[r-2]+i[r-1]+i[r]=='BAD': 
        k += 1
    while k == 3:
        m = min(m, r-l+1)
        if i[l]+i[l+1]+i[l+2]=='BAD':
            k -=1
        l += 1
print(m)