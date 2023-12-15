import sys

N, M = map(int, input().split())

alllist = []

for i in range (N) : 
    compolist = list(map(int, sys.stdin.readline().split()))
    alllist.append (compolist)
    
K = int(input())

for _ in range (K) :
    i, j, x, y = map(int, sys.stdin.readline().split())
    tempy = y
    
    suma = 0 
    
    while True : 
        suma += alllist[x - 1][y - 1]
        
        if i == x and j == y :
            break
        
        if y == j :
            x = x - 1
            y = tempy
            
        else : 
            y = y - 1
            
    print (suma)