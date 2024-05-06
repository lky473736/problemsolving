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

while True :
    try : 
        p, q, r = map(int, sys.stdin.readline().split())
        up = p * q
        down = r - q
        
        gcd = euclidean(up, down)
        
        up = up // gcd
        down = down // gcd
        
        print (f'{up}/{down}')
        
    except :
        break