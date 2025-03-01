l = open('24_10105.txt').readline()
left = m = k = 0
for right in range(0, len(l)):
    if l[right]=='T': k+=1
    while k>100:
        if l[left]=='T': k-=1
        left += 1
    m = max(m, right-left+1)
print(m)

l = open('24_13715.txt').readline()
left = m = k = 0
for right in range(1,len(l)):
    if l[right-1]+l[right]=='AB': k += 1
    while k > 50: 
        if l[left]+l[left+1]=='AB': k -=1
        left += 1
    if k == 50: m = max(m, right-left+1)
print(m)