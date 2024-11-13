import sys
import math

max_cur = [0, 0]

for i in range (1, 1000001) :
    cur = i
    cnt = 0
    
    while True : 
        if cur == 1 :
            print (i, cnt)
            
            if cnt > max_cur[0] : 
                max_cur[0] = cnt
                max_cur[1] = i
                
            break
                
        else : 
            if cur % 2 == 0 : 
                cur //= 2
            
            else : 
                cur = 3 * cur + 1
                
            cnt += 1
                
print (max_cur)
