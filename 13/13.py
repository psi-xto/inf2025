from ipaddress import *
for mask in range(10,32):
    a = ip_network(f'121.96.174.205/{mask}',0)
    c = 0
    for i in a:
        i = f'{i:b}'
        if i.count('1')==12:
            c += 1
    if c == 10:
        print(mask)
