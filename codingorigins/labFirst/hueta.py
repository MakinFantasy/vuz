from math import *


counter = 0
while counter != 5:
    a1 = float(input())
    z1 = ((cos(3/8*pi - a1/4))**2) - ((cos(11/8*pi + a1/4))**2)
    print(z1)
    counter += 1

print('----------------------------------------------------------')

counter2 = 0
while counter2 != 5:
    a2 = float(input())
    z2 = (sqrt(2)/2)*(sin(a2/2))
    print(z2)
    counter2 += 1

print('finished')
