from re import *

a = open("24_17563.txt").readline()
num = r"[1-9][0-9]*"
pat = rf"{num}([-*]{num})+"
m = max([x.group() for x in finditer(pat, a)], key=len)
print(len(m))
