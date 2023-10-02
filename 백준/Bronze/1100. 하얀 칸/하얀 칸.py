count = 0

for i in range (8) :
    chess = input()
    
    if i % 2 == 0 :
        j = 0
    
    else :
        j = 1
    
    for j in range (j, 8, 2) :
        if chess[j] == 'F' :
            count += 1
            
        else :
            pass
        
print (count)