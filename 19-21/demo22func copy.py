def f(a,n):
    if a <= 17: 
        return n%2==0
    if n == 0: return False
    moves = [f(a-1,n-1), f(a//3 if a%3==0 else a-2,n-1), f(a//5 if a%5==0 else a-3,n-1)]
    if n % 2 == 0:
        return all(moves)
    return any(moves)

for S in range(20,100):
    if not f(S,2) and f(S,4):
        print(S)