import sys
'''sys.setrecursionlimit(10**6)

def factorial (n) : 
    if n == 0 :
        return 1
        
    else :
        return n * factorial(n - 1)'''

while True :
    n, k = map(int, sys.stdin.readline().split())
    
    if n == k and n == 0 and k == 0 :
        break
    
    if n - k < k :
        k = n - k
        
    rst = 1
    
    for i in range (1, k + 1) :
        rst *= n
        n -= 1
        rst /= i
    
    # print (factorial(n) // (factorial(k) * factorial(n - k)))
    
    print (int(rst))
    
    '''fn, fk, fnk = n, k, n-k
    nfn, nfk, nfnk = 1, 1, 1
    
    while True :
        if fn == 0 :
            break
        
        else :
            nfn *= fn
            fn -= 1
            
    while True :
        if fk == 0 :
            break
        
        else :
            nfk *= fk
            fk -= 1
            
    while True :
        if fnk == 0 :
            break
        
        else :
            nfnk *= fnk
            fnk -= 1
            
    print (nfn // (nfk * nfnk))'''
    
'''def factorial (n) : 
    if n == 0 :
        return 1
        
    else :
        return n * factorial(n - 1)'''