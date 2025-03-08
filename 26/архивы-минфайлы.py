l = open('26_813.txt')
s, n = map(int,l.readline().split())
files = sorted([int(i) for i in l.readlines()])
a = []
print(min(files))
while sum(a)+files[0]<=s:
    for i in range(len(files)-1, 0, -1):
        if sum(a)+files[i]<=s:
            a += [files[i]]
            files.pop(i)
            break
    if sum(a)+files[0]<=s:
        a += [files[0]]
        files.pop(0)
print(a)
print(len(a), a[-1])