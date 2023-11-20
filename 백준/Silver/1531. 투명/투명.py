import sys

N, M = map(int, sys.stdin.readline().split())

suma = 0

slist = [[0 for i in range(100)] for j in range (100)]

for i in range (N) : 
    x, y, p, q = map(int, sys.stdin.readline().split())
    
    for j in range (x, p + 1) :
        for k in range (y, q + 1) :
            slist[k - 1][j - 1] += 1
            
for p in range (100) : 
    for q in range (100) : 
        if slist[p][q] > M : 
            suma += 1
    
print (suma)