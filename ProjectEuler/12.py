import sys
import math

prev = 0
y = 0
for x in range (1, 10000000) :
    y += x
    print (y)
    slist = []
    cnt = 0
    
    for i in range(1, int(math.sqrt(y)) + 1):
        if y % i == 0 :
            slist.append(i) 
            cnt += 1
            
            if i != y // i :          
                slist.append(y // i)
                cnt += 1
                
    if len(slist) >= 500 : 
        print ("final : ", y) 
        break
    
    
