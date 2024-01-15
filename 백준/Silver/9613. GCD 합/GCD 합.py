import sys
import itertools

def euclidean (X, Y) :
    a = Y 
    b = X % Y 
    p = 0
    
    if b == 0 :
        return a
    
    while True :
        p = a % b
        
        if p == 0 :
            break
        
        a = b
        b = p
        
    return b
    
t = int(sys.stdin.readline())
    
for _ in range (t) : 
    list_num = list(map(int, sys.stdin.readline().split()))
    list_num.pop(0)
    list_combi = itertools.combinations(list_num, 2)
    
    suma = 0
    
    for i in list_combi : 
        suma += euclidean (i[0], i[1])
        
    print (suma)