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

a, b = map(int, sys.stdin.readline().rstrip().split(':'))

print (f'{a // euclidean(a, b)}:{b // euclidean(a, b)}')