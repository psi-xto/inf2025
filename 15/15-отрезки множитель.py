P = [int(i)/4 for i in range(10,26)]
Q = [int(i)/4 for i in range(15,31)]
R = [int(i)/4 for i in range(25,41)]
A = [] # минимальная длина
for x in range(0,10000):
    x = x/4
    if (((x in Q) <= (x not in R)) and (x in A) and (x not in P))==0:
        A += [x]
print(A)
print(len(A))

# проверяем включительность и домножаем на множитель