A, B = map(int, input().split())

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

gcd = euclidean(A, B)
print(gcd)
print(A * B // gcd)