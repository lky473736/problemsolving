# queue

import time
T = int(input())

for i in range (T) : 
    N, M = map(int, input().split())
    
    weight = list(map(int, input().split()))
    weight = [(x+1, weight[x]) for x in range (N)]
    counting = 0
    
    while True : 
        maxvalue = max(item[1] for item in weight)
        
        if weight[0][1] == maxvalue : 
            if weight[0][0] == M + 1 : 
                print (counting + 1)
                break
            
            weight.pop(0)
            counting += 1
        
        else :
            temp = weight[0]
            weight.pop (0)
            weight.append (temp)
            
