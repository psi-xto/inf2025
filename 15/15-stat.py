P = [int(i) for i in range(3,44)]
Q = [int(i) for i in range(18,92)]
R = [int(i) for i in range(72,116)]
step = sorted([3,43,18,91,72,115])
res = []
for s in step:
    for e in step:
        A = [int(i) for i in range(s,e)]
        f = 1
        for x in range(200):
            f*=(x in Q) <= ((not(x in P)) <= (((not(x in R)) and (not (x in A))) <= (not (x in Q))))
        if f == 1:
            res.append(e-s)
print(res)


P = [int(i) for i in range(17,59)]
Q = [int(i) for i in range(29,81)]
steps = [17, 29, 58, 80]
res = []
for s in steps:
    for e in steps:
        A = [int(i) for i in range(s,e)]
        f = 1
        for x in range(1000):
            f *= ((x in P) <= (((x in Q) and not(x in A)) <= (not(x in P))))
        if f == 1:
            res.append(e-s)
print(res)