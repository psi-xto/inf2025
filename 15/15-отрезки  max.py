P = [int(i) for i in range(15,40)] # ко второй границе +1 надо прибавлять
Q = [int(i) for i in range(45,48)]
A = [int(i) for i in range(10000)] # макс длина та же, что и по ренжу ниже
for x in range(0,10000):
        # если тождественно ИСТИНА, ставишь not в начале; ЛОЖНА - просто переписываешь выражение
        if not((x in A) <= (x in P)) or (x in Q): 
            A.remove(x)
print(A)
print(len(A)-1) # минус один для максимального
