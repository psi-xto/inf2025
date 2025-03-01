from functools import lru_cache
def moves(h):
    return h+1,h**2
@lru_cache(None)
def game(h):
    if h >= 100: return('W')
    if any(game(j)=='W' for j in moves(h)): return('P1')
    if any(game(j)=='P1' for j in moves(h)): return('B1') # P1 неудачный по усл
    if any(game(j)=='B1' for j in moves(h)): return('P2')
    if all(game(j)=='P1' or game(j)=='P2' for j in moves(h)): return('B2')

for x in range(2,200):
    if game(x)=='B1':
        print(x, game(x))