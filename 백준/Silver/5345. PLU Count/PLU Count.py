import sys

N = int(sys.stdin.readline())

for i in range (N) :
    line = sys.stdin.readline().rstrip()
    
    token = 0
    counting = 0
    
    for char in line : 
        if token == 0 and (char == 'p' or char == 'P') :
            token = 1
            continue
        
        if token == 1 and (char == 'l' or char == 'L') : 
            token = 1.5
            continue
        
        if token == 1.5 and (char == 'u' or char == 'U') : 
            token = 2
            
        if token == 2 : 
            counting += 1
            token = 0
            
    print (counting)