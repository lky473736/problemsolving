# chun-hyang

n = int(input())

if n < 5 : # 5보다 작을 때
    if n == 2 or n == 4 :
        print (n // 2)
        exit()
        
    else :
        print (-1)
        exit()
        
if (n % 5) == 0 : # 5로 나눌 수 있을 때
    print (n // 5)
    exit()
    
if (n % 5) % 2 == 0 : # 5로 나누고 나머지가 2로도 나누어질 때
    print ((n // 5) + ((n % 5) // 2))
    exit()
        
else : # 5로 나누고 나머지가 2로 나누어지지 않을 때
    f = 0
    t = 0
    finder = []
    
    for i in range (n // 5) :
        f = i + 1
        t = (n - f * 5) // 2
        
        if f * 5 + t * 2 == n :
            finder.append (f + t)
    
    if finder == [] :
        if n % 2 == 0 :
            print (n // 2)
            
    if finder != [] : 
        print (min(finder))