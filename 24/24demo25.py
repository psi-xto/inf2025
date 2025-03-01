a = open('24-300.txt').readline()
a = (a.replace('++','X').replace('+*','X')
     .replace('*+','X').replace('**','X').split('X'))
# отбрасываем двойной знак сразу, осталось только проверить валидность
m = 0
eval0 = []
neval0 = []
for i in range(0, len(a)):
    c = 0
    if a[i][-1]!='*' and a[i][0]!='*' and a[i][-1]!='+' and a[i][0]!='+':
        c += len(a[i])
        eval0.append(a[i]) # первоначальный массив со всем
for i in eval0:
    if eval(i)==0:
        m = max(m, len(i))
    elif len(i)>2:
        for x in range(0, len(i)-1):
            for y in range(x, len(i)):
                neval0.append(i[x:y]) # срезы подстрок от строк не равных 0
for i in neval0:
    if len(i) > 2 and i[-1] != '*' and i[0] != '*' and i[-1] != '+' and i[0] != '+' and i != '':
        try:
            eval(i) # костыль
        except:
            i = '0'
        if eval(i) == 0:
            ###print(i, len(i))
            m = max(m, len(i))
print(m)