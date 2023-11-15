slist = [i for i in range (1, 10001)]

def kaprekar (n) :
    leng = len(str(n))
    
    sumation = n
    
    for i in str(n) : 
        sumation += int(i)
        
    return sumation
    
for i in range (0, 10000) : 
    if kaprekar(i) in slist :
        slist.remove (kaprekar(i))
        
for j in slist :
    print (j)