P = [i for i in range(3, 44)]
Q = [i for i in range(18, 92)]
R = [i for i in range(72, 116)]
point = [3, 18, 43, 72, 91, 115]
res = []
for s in point:
    for e in point:
        f = 1
        A = [i for i in range(s, e)]  # минимальная длина
        for x in range(1, 200):
            f *= (x in Q) <= (
                (not (x in P))
                <= (((not (x in R)) and (not (x in A))) <= (not (x in Q)))
            )
        if f == 1:
            res.append(e - s)
print(res)
print(len(res))

from itertools import *


def f(x):
    A = a1 <= x <= a2
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    return C <= (((not A) and B) <= (not C))


Ox = [i / 4 for i in range(20 * 4, 120 * 4)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)
print(min(m))
