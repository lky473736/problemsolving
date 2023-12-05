N = int(input())

state = 0
i = 0

while N != 0 :
    if i % 2 == 0 : 
        state = 0 # sk
        
    else : 
        state = 1 # cy

    if N > 3 :
        N -= 3
    
    else :
        if N == 2 :
            if state == 0 : 
                print ("CY")
                
            else : 
                print ("SK")
                
        else : 
            if state == 0 : 
                print ("SK")
                
            else :
                print ("CY")
                
        break
        
    i += 1 # for check the turn
    
