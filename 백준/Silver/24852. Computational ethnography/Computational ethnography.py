import sys
import math

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

counting = 0
i = 1

'''while (i ** 2) < A :
    i += 1'''

while (i ** 2) <= B : 
    if (i ** 2) >= A : 
        stri = str(i ** 2) 
        
        '''if 0 < int(stri) and int(stri) < 10 : # 1자리일 때
            if math.sqrt(int(stri)) == int(math.sqrt(int(stri))) :
                counting += 1
                # print (stri)
                
        else : # 2자리 이상일 때'''
        
        stri = stri[::-1]
            
        if stri[0] != '0' and int(stri) == int(math.sqrt(int(stri))) ** 2 : 
            counting += 1
            
    i += 1

print (counting)