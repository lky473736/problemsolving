'''N = int(input())
 
i = 2
    
while N / i != 1 :
    if N % i == 0 :
        print (i)
        N = N / i
        
    else : 
        i += 1
    
print (i)'''

import sys
N = int(sys.stdin.readline())

if N == 1 : 
    exit()
 
i = 2
    
while N / i != 1 :
    if N % i == 0 :
        print (i)
        N /= i
        
    else : 
        i += 1
    
print (i)
