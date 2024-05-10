import sys

T = int(sys.stdin.readline())

for i in range (T) :
    B, D = map(str, sys.stdin.readline().split())
    
    suma = 0 
    for j in D :
        suma += int(j)
        
    print (suma % (int(B)-1))