import sys

N = int(sys.stdin.readline())
L = int(sys.stdin.readline())

snail = [[0 for j in range (N)] for i in range (N)]

i = 0
j = 0
K = N ** 2 
boundary = N 
P = boundary 

position_L = [0, 0]

# 아래 오른 위 왼
mode = 0

while K != 0 :
    snail[i][j] = K
    
    if K == L :
        position_L[0], position_L[1] = i, j  
        
    K -= 1
    boundary -= 1
    
    if boundary == 0 : 
        if mode == 0 :
            mode = 1
            
        elif mode == 1 :
            mode = 2
            
        elif mode == 2 :
            mode = 3
            
        elif mode == 3 :
            mode = 0
            
        boundary = N - 1
            
    if mode == 0 :
        i += 1
            
    elif mode == 1 :
        j += 1
            
    elif mode == 2 :
        i -= 1
            
    elif mode == 3 :
        if boundary == 1 :
            N -= 2
            boundary = N
            i += 1
            mode = 0
            
        else :
            j -= 1
            
for i in snail : 
    print (*i)
    
print (position_L[0]+1, position_L[1]+1)