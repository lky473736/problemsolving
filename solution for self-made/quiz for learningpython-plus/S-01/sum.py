def ssum(slist) :
    s = 0
    
    for i in range (len(slist)) :
        s = s + slist[i]
        
    return s

print (ssum([1, 2, 3, 4, 5]))