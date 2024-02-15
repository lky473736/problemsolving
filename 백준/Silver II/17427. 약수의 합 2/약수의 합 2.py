'''import sys

N = int(sys.stdin.readline())

a = 0

for i in range (1, N + 1) : 
    seta = set()
    b = 0
    
    if i == 1 :
        b += 1
        
    else :
        j = 1
        
        while True : 
            if i // j in seta :
                break
            
            if i % j == 0 :
                b += j
                
                if j ** 2 != i : 
                    b += i // j
                    
                seta.add (j)
                
            j += 1
            
    a += b
            
print (a)'''

import sys

N = int(sys.stdin.readline())
print (sum(k*(N//k) for k in range (1, N+1)))