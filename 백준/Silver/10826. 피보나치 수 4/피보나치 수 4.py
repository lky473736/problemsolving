import sys

n = int(sys.stdin.readline())

t1, t2 = 0, 1

if n <= 1 : 
    if n == 0 : 
        print (0)
    
    elif n == 1 :
        print (1)
        
else :
    k = 1
    
    n -= 2
    t = 0
    
    while n != 0 :
        k = t1 + t2
        t1 = t2
        t2 = k
        
        if t == 0 :
            t = 1
            continue
        
        n -= 1

    print (k)