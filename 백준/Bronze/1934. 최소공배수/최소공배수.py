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
    
T = int(input())

for i in range (T) :
    A, B = map(int, input().split())
    gcd = euclidean(A, B)
    
    print ((A * B) // gcd)