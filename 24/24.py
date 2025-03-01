a = open('24_223.txt').readline().replace('TIK','TOK')
k = m = 0
for i in range(len(a)):
    if (a[i:i+3]) == 'TOK': 
        k += 1
print(k)