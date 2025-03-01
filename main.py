from ipaddress import *
c = 0
a = ip_network(f'10.48.96.0/255.255.240.0',0)
for i in a:
    b = f'{i:b}'
    if b.count('1')>b.count('0'):
        c += 1
print(c)