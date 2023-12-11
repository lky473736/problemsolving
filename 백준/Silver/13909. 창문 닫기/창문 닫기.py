'''for N in range (1, 17) :
    slist = [0 for i in range (N)]
    while N != 0 :
        lp = len(slist) // N
        
        for i in range (lp) : 
            if slist[N + i * N - 1] == 0 :
                slist[N + i * N - 1] = 1
                
            else :
                slist[N + i * N - 1] = 0
                
        N -= 1
        
    print (slist)
    
    2, 4, 6, 8, ...
    
    '''
    
N = int(input())

cur = 1 
zeronum = 0

while N != cur + zeronum : 
    if cur * (cur + 1) == zeronum :
        cur += 1
        
    else :
        zeronum += 1
    
print (cur)