def f(a,b,n): # камни в куче номер хода
    if a+b <= 20 or n > 4: #число с которого нужно выиграть,  мансуем с n 2-4 строки
        return n == 4 or n == 2
    if n % 2 == 0:
        return all([f(a-1,b,n+1),f(a//2+a%2,b,n+1),f(a,b-1,n+1),f(a,b//2+b%2,n+1)]) # противник neумный any
    return any([f(a-1,b,n+1),f(a//2+a%2,b,n+1),f(a,b-1,n+1),f(a,b//2+b%2,n+1)])
for s in range(100, 10, -1):
    if f(s,10,0):
        print(s)