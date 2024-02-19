def fibo(n) :
    a, b = 0, 1
    
    for _ in range(2, n+1) :
        a, b = b%1000000007, (a+b)%1000000007
        
    return b

n = int(input())

if n == 0 :
    print (0)
    
else :
    print (fibo(n))