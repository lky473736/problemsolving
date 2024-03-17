while True :  
    try :
        X = int(input())
        
        slist = [[1]]
        
        start, p = 2, 1
        
        while True : 
            if X in slist[-1] :
                break
            
            if p % 2 != 0 :
                slist.append (list(range(start, start + p + 1)))
            
            else :
                slist.append (list(reversed(list(range(start, start + p + 1)))))
                
            start = start + p + 1
            
            p = p + 1
        
        numerator = slist[p - 1].index(X) + 1
        denominator = p - slist[p - 1].index(X)
        
        print (f"TERM {X} IS", str(numerator) + '/' + str(denominator))
        
    except :
        exit()