a = open('24.txt').readline().split('T')
m = 10**9
for i in range(0, len(a)-210):
    r = 'T'.join(a[i:i+209]) # 208 элементов
    m = min(len(r)+2,m) # можем по 2 буквы в начало и конец
print(m)
