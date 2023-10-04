T = int(input())

for i in range (T) :
    suma = 0
    
    N = int(input())
    
    for i in range (1, N + 1, 2) :
        suma += i
    
    print (suma)