import sys
import math

suma_square = 0
suma = 0
for i in range (1, 101) :
    suma_square += i**2
    suma += i
    
print (suma**2, suma_square)
print (suma**2 - suma_square)
