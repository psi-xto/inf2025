def f(x,y,i): # x,y - нач,кон; i = номер команды
    if x>y: return 0
    if x == y and i == 7: return 1
    else: return f(x+1,y,i+1)+f(x+4,y,i+1)+f(x*2,y,i+1)
print(f(3,27,0))
