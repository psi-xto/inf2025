def f(x,y,i): # i - счетчик интересующей команды
    if x > y: return 0
    if x == y: return i<=3
    if x < y: return f(x+2,y,i)+f(x*3,y,i+1)+f(x*5,y,i+1)
print(f(2,200,0))