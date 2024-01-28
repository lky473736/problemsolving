import sys
import itertools

N = int(sys.stdin.readline())

'''while True : 
    sequence = [1]
    
    while True : 
        if counting == N : 
            break
        
        i += j
        
        if sequence[-1] != i :
            if (sequence[-1] * i) % (sequence[-1] + i) != 0 :
                sequence.append (i)
                counting += 1
                i = sequence[-1]
                
                print (sequence)
            
            else :
                i = 1
                j += 1
                break
            
        else :
            j += 1
            break
            
    if counting == N : 
        
        break'''
        
k = 1

while True :
    breakkey = 0
    
    sequence = [1 + j*k for j in range (N)]
    
    combi = itertools.combinations(sequence, 2)
    
    for i in combi : 
        if (i[0] * i[1]) % (i[0] + i[1]) == 0 :
            breakkey = 1
            break
        
    if breakkey == 1 :
        k += 1
        
    else :
        break
    
print (*sequence)