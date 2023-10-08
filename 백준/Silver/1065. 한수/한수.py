X = int(input())

counting = 0
i = 0

while X >= i :
    counting2 = 0
    
    if len(str(i)) != 1 :
        for j in range (len(str(i)) - 1) :
            if j == 0 :
                p = int(str(i)[0]) - int(str(i)[1])
                counting2 += 1
            
            else :
                if p == int(str(i)[j]) - int(str(i)[j + 1]) :
                    counting2 += 1
                    
                else :
                    break
        
        if counting2 == len(str(i)) - 1 :
            counting += 1
        
        else : 
            pass
    
    else : 
        counting += 1
    
    i += 1 
    
print (counting -1 )