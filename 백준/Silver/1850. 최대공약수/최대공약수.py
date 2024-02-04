import sys

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
    
A, B = map(int, sys.stdin.readline().split())
counting = euclidean(A, B)

for i in range (counting) : 
    print ('1', end = '')