def sany (k) :
    zerocount = 0
    
    for i in k :
        if i == 0 :
            zerocount = zerocount + 1
    
    if zerocount == len(k) :
        return False
    
    else :
        return True

print (sany([1, 2, 3, 4, 5, 0]))
print (sany([0, 0, 0]))