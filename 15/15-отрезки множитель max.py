P = [int(i)/10 for i in range(10,26)]
Q = [int(i)/10 for i in range(15,31)]
R = [int(i)/10 for i in range(25,41)]
A = [int(i)/10 for i in range(1000)] # макс длина та же что и по ренжу ниже
for x in range(0,1000):
        x = x/10
        if (((x in Q) <= (x not in R)) and (x in A) and (x not in P)):
            A.remove(x)
print(A)
print(len(A)-1)
print('123')
# проверяем включительность и домножаем на множитель