# hello dogyeom

while True : 
    N = input()
    
    if N == '0' :
        break
    
    k = 0
    
    while len(N) != 1 :
        for i in N : 
            k = k + int(i)
            
        N = str(k)
        k = 0
        
    print (N)