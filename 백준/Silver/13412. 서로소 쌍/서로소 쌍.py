import sys
import math

def euclidean (X, Y) :
    a = Y 
    b = X % Y 
    p = 0
    
    if b == 0 :
        return a
    
    while True :
        p = a % b
        
        if p == 0 :
            break
        
        a = b
        b = p
        
    return b

T = int(sys.stdin.readline())

for _ in range (T) :
    N = int(sys.stdin.readline())
    
    if N == 1 :
        print (1)
        continue
    
    counting = 0
    
    recent = []

    for i in range (1, N) : 
        if i == 1 :
            counting += 1
            continue
        
        if N % i == 0 : 
            if euclidean(i, N // i) == 1 :
                if recent == [N // i, i] : 
                    break
                
                recent = [i, N // i]
                counting += 1
                
    print (counting)
    