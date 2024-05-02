import sys
import math

a, b, h = map(int, sys.stdin.readline().split())

if a == 0 and a == b : 
    print (-1)
    exit()

k1 = math.sqrt(a**2 + (a*h / (b-a))**2)
k2 = math.sqrt(h**2 + (b-a)**2)

rst = math.pi * ((k1 + k2)**2 - k1**2)

if rst != 0 :
    print (rst)
    
else : 
    print (-1)