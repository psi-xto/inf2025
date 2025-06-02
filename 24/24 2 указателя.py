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
