from ipaddress import *
c = 0
a = list(ip_network('192.168.32.160/255.255.255.240'))
for i in a:
    if bin(int(i))[2:].count('1')%2==0:
        c+=1
print(c)