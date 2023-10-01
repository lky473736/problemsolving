while True : 
    n = int(input())
    
    if n == -1 :
        break
    
    slist = []
    
    for i in range (n) :
        if n % (i + 1) == 0 :
            slist.append (i + 1)
            
    slist.remove(slist[-1])
    
    if sum(slist) == n :
        print (f"{n} = ", end = '')
        
        for i in range (len(slist)) :
            if len(slist) - 1 == i :
                print (f"{slist[i]}")
            
            else :
                print (f"{slist[i]} + ", end = '')
                
    elif sum(slist) != n :
        print (f"{n} is NOT perfect.")
