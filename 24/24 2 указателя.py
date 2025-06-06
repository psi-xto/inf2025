l = open("24_10105.txt").readline()
left = m = k = 0
for right in range(0, len(l)):
    if l[right] == "T":
        k += 1
    while k > 100:
        if l[left] == "T":
            k -= 1
        left += 1
    m = max(m, right - left + 1)
print(m)

l = open("24_13715.txt").readline()
left = m = k = 0
for right in range(1, len(l)):
    if l[right - 1] + l[right] == "AB":
        k += 1
    while k > 50:
        if l[left] + l[left + 1] == "AB":
            k -= 1
        left += 1
    if k == 50:
        m = max(m, right - left + 1)
print(m)

l = open("24_12476.txt").readline()
left = m = k = 0
for right in range(1, len(l)):
    if right >= 2:
        if (
            l[right - 2] + l[right - 1] + l[right] == "ORO"
            or l[right - 2] + l[right - 1] + l[right] == "ROR"
        ):
            k = 0
            left = right - 1
    if l[right - 1] + l[right] == "RO":
        k += 1
    while k > 21:
        if l[left] + l[left + 1] == "RO":
            k -= 1
        left += 1
    if k == 21:
        m = max(m, right - left + 1)
print(m)

a = open("24_9169.txt").readline()
k = 0
m = 10**9
l = 0

for r in range(2, len(a)):
    if a[r - 2 : r + 1] in ("BAD", "FAT"):
        k += 1
    while k == 3:
        m = min(m, r - l + 1)
        if a[l : l + 3] in ("BAD", "FAT"):
            k -= 1
        l += 1
print(m)
