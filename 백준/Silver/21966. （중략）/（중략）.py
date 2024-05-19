import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

if N <= 25 : 
    print (S)
    
else : 
    '''
    if N == 25 : 
        print (f"{S[:10]}......{S[-11:]}")
        
    else : 
        print (f"{S[:11]}...{S[-11:]}")'''
        
    token = 0
    
    # print (S[11:-11])
    for i in range (N - 22) :
        char = S[11+i]
        # print (char, N - 2)
        
        if char == '.' : 
            if i < N - 22 - 1 :
                token = 1 
            
            break 
        
    if token == 1 : 
        print (f"{S[:9]}......{S[-10:]}")
        
    else : 
        print (f"{S[:11]}...{S[-11:]}")