from fnmatch import *
for i in range(0, 10 ** 10, 4173):
    if fnmatch(str(i), '1?2655*8'):
        print(i)