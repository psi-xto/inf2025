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

import itertools

m = 0
a = open("2.txt").readline()
for i in itertools.product("QRS", repeat=2):
    z = "".join(i)
    a = a.replace(z, z[0] + " " + z[1])
for i in a.split():
    m = max(len(i), m)
print(m)

m = 1
c = 1
a = open("2.txt").readline()
for i in range(0, len(a) - 1):
    if a[i] not in "QRS" or a[i + 1] not in "QRS":
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)

m = 0
a = open("3.txt").readline().split("FSRQ")
for i in range(0, len(a) - 79):
    s = "FSRQ".join(a[i : i + 81])
    m = max(m, len(s))
    if len(s) == 2373:
        print(s.count("FSRQ"))
print(m + 6)

a = open("4.txt").readline()
k = 0
m = 10**12
l = 0
for r in range(0, len(a)):
    if a[r] == "Y":
        k = 0
        l = r + 1
    if a[r] == "X":
        k += 1
    while k >= 500:
        m = min((r - l + 1), m)
        if a[l] == "X":
            k -= 1
        l += 1
print(m)

a = open("5.txt").readline().split("RSQ")
k = 0
m = 10**12
for i in range(0, len(a) - 129):
    s = "RSQ".join(a[i : i + 131])
    if not s[-1] == "Q":
        m = min(m, len(s))
    if len(s) == 501:
        print(s)
print(m - 4)

a = open("5.txt").readline()
k = 0
m = 10**12
l = 0
for r in range(3, len(a)):
    if a[r - 3 : r] == "RSQ":
        k += 1
    while k == 130:
        s = a[l : r + 1]
        if s[-1] != "Q":
            m = min(m, len(s))
        if a[l : l + 3] == "RSQ":
            k -= 1
        l += 1
print(m)

from re import *

a = open("6.txt").readline()
pat = r"[1-B][0-B]*[13579B]"
m = max([i.group() for i in finditer(pat, a)], key=lambda x: int(x, 12))
print(a.find(m))

from re import *

m = 0
a = open("7.txt").readline()
pat = r"[1-F][0-F]*[0-F]"
for i in finditer(pat, a):
    i = i.group()
    l = 0
    k = 0
    for r in range(0, len(i)):
        if i[r] == "B":
            k += 1
        while k > 10:
            if i[l] == "B":
                k -= 1
            l += 1
        if k == 10:
            m = max(m, r - l + 1)
print(m)

from re import *

a = open("8.txt").readline()
num = r"([1-9][0-9]*|0)"
pat = rf"{num}([-*]{num})+"
print((max([i.group(0) for i in finditer(pat, a)], key=len)))

m = 0
a = (
    open("../9.txt")
    .readline()
    .replace("++", "!")
    .replace("*+", "!")
    .replace("+*", "!")
    .replace("**", "!")
)
for i in "123456789":
    a = a.replace(i, "1")
for c in a.split("!"):
    if len(c) > m:
        for i in range(len(c) - 1):
            if c[i] not in "+*" and c[i] not in ("0", "0"):
                substring = c[i]
                for j in range(i + 1, len(c)):
                    substring += c[j]
                    if substring[-1] not in "+*" and eval(substring) == 0:
                        m = max(m, len(substring))
                        if len(substring) == 169:
                            print(substring)
print(m)

from re import *

m = 0
a = open("9.txt").readline()
num = r"([1-9][0-9]*|0)"
pat = rf"{num}([+*]{num})+"
for i in finditer(pat, a):
    i = i.group()
    if len(i) > m:
        for x in range(len(i) - 1):
            if i[x] not in "+*" and i[x : x + 2] not in (
                "00",
                "01",
                "02",
                "03",
                "04",
                "05",
                "06",
                "07",
                "08",
                "09",
            ):
                substring = i[x]
                for j in range(x + 1, len(i)):
                    substring += i[j]
                    if substring[-1] not in "*+" and eval(substring) == 0:
                        m = max(m, len(substring))
                        if len(substring) == 167:
                            print(substring)
print(m)

from re import *

m = 0
a = open("10.txt").readline()
first = r"([A-Z]{1})([a-z]*)"
word = r"([A-Z]{0,1}([a-z]+))"
sent = rf"({first})( {word})+([.])"
print(sent)
for i in finditer(sent, a):
    i = i.group()
    m = max(m, len(i))
print(m)
