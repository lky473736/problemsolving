T = int(input())

for p in range (T) :
    N = int(input())
    state = 0
    
    if N == 0 :
        state = 'INSOMNIA'
        
    else : 
        slist = []
        num = 0
        i = 1
        
        while True : 
            if 1 in slist and 2 in slist and 3 in slist and 4 in slist and 5 in slist and 6 in slist and 7 in slist and 8 in slist and 9 in slist and 0 in slist:
                state = N * (i - 1)
                break
            
            compo = list(str(N * i))
            scompo = [int(x) for x in compo]
            
            for k in scompo : 
                if k not in slist : 
                    slist.append(k)
                    
            i += 1
    
    print (f"Case #{p+1}:", state)