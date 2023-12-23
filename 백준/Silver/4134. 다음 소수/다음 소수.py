import sys
import math

T = int(sys.stdin.readline().rstrip())

for _ in range (T) :
    n = int(sys.stdin.readline().rstrip())
    
    if n != 1 and n != 0 :
        while True :
            notprime = 0
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0 :
                    notprime = 1
                    break
                
            if notprime == 1 :
                n += 1
                
            else :
                break
            
        print (n)
        
    else : 
        print (2)