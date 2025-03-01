for A in range(0,1000):
    if all((((x + 2*y) < A) or (y > x) or (x > 60)) for x in range(0,100) for y in range(0,100)):
        print(A)