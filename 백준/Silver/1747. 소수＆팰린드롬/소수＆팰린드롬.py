import math
    
N = int(input())

if N == 1 :
    print (2)
    exit()

while True :
    passcode = 0
        
    if str(N) == str(N)[::-1] :
        passcode = 1
    
    if passcode == 1 :    
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0 :
                passcode = 2
                break
        
        if passcode == 1 :
            break 
        
    N += 1
        
print (N)