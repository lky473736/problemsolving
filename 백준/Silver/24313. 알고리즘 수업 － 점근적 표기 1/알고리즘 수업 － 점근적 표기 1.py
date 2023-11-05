a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 <= 0 :
    print (1)
    exit()

if (a1 * n0 + a0) <= (c * n0) :
    finder = 0 
    
    for i in range (n0, 101) :
        if (a1 * i + a0) <= (c * i) : 
            finder += 1
        
    if finder == 100 - n0 + 1 :
        print (1)
    
    else :
        print (0)
    
else :
    print (0)