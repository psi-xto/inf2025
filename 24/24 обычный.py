a = open("24_58329.txt").readline()
c = 2  # сумма двух идущих подряд, берем 2
m = 0
for i in range(0, len(a) - 2):
    if int(a[i]) + int(a[i + 1]) > int(a[i + 2]):
        c += 1
    else:
        m = max(c, m)
        c = 2
print(m)

a = open("69932.txt").readline()
c = 0
m = 0
for i in range(0, len(a) - 1):
    if a[i] in "0678" or (a[i - 1] in "678" and a[i + 1] in "678" and c != 0):
        c += 1
    else:
        m = max(m, c)
        c = 0
print(m)
