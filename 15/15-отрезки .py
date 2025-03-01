P=[i for i in range(3,44)]
Q=[i for i in range(18,92)]
R=[i for i in range(72,116)]
point=[3,18,43,72,91,115]
res = []
for s in point:
      for e in point:
        f = 1
        A = [i for i in range(s,e)] # минимальная длина
        for x in range(1,200):
            f *= ((x in Q) <= ((not(x in P)) <= (((not(x in R)) and (not (x in A))) <= (not (x in Q)))))
        if f == 1:
            res.append(e-s)
print(res)
print(len(res)) 