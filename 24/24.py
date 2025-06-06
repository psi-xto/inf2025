a = open("1.txt").readline()
c = m = 0
sogl = "BCD"
for i in sogl:
    a = a.replace(i, "B")
gl = "AO"
for j in gl:
    a = a.replace(j, "A")
from re import *

pat = r"(BA)+"
for i in finditer(pat, a):
    m = max(i.group().count("BA"), m)
print(m)

a = open("1.txt").readline()
c = m = 0
sogl = "BCD"
for i in sogl:
    a = a.replace(i, "B")
gl = "AO"
for j in gl:
    a = a.replace(j, "A")
a = a.replace("BA", "!")
for i in range(0, len(a)):
    if a[i] == "!":
        c += 1
    else:
        m = max(m, c)
        c = 0
print(m)

a = open("1.txt").readline()
c = m = 0
sogl = "BCD"
for i in sogl:
    a = a.replace(i, "B")
gl = "AO"
for j in gl:
    a = a.replace(j, "A")
r = [0] * len(a)
for i in range(0, len(a) - 1, 2):
    if a[i] + a[i + 1] == "BA":
        r[i + 1] = r[i - 1] + 1
print((r))
