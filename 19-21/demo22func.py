def f(a,n): # камни в куче номер хода
    if a >= 29 or n > 2: #число с которого нужно выиграть,  мансуем с n 2-4 строки
        return n==2 or n==4
    if n % 2 == 0:
        return all([f(a+1, n+1),f(a*2,n+1)]) # противник умный
    return any([f(a+1,n+1),f(a*2,n+1)])
for s in range(1,29):
    if f(s,0):
        print(s)