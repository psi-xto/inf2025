def F(x):
    C = 29 <= x <= 100
    D = 7 <= x <= 68
    A = a1 <= x <= a2
    return (D) <= ((not C and not A) <= (not D))


res = []
d = [y for x in [29, 7, 68, 100] for y in [x - 0.1, x + 0.1, x]]
for a1 in d:
    for a2 in d:
        if a2 > a1:
            if all(F(x) == 1 for x in d):
                res.append(a2 - a1)
print(round(max(res)))
