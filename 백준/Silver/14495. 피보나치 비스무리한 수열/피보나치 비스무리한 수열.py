import sys

n = int(sys.stdin.readline())

sequence = [1, 1, 1]

if 1 <= n and n <= 3 : 
    print (1)
    
else :
    counting = 3
    
    while counting != n :
        sequence.append (sequence[counting-1] + sequence[counting-3])
        counting += 1
        
    print (sequence[-1])