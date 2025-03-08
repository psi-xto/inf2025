f = open('26_936.txt')
n,s = map(int, f.readline().split())
data = sorted([int(i) for i in f.readlines()],reverse=True)
c = 0
z = 0
last = 0
while len(data)>0:
    for i in range(len(data)):
        if z + data[i] <= s:
            z += data[i]
            data[i] = 0
    data = [x for x in data if x !=0]
    c += 1
    last = z
    z = 0
print(c,last)