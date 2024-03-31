import sys

nums = []

'''while True : 
    try : 
        N = int(sys.stdin.readline())
        nums.append (N)
        
    except : 
        break'''
        
for line in sys.stdin:
    N = int(line)
    nums.append (N)

for K in nums :  
    N = K
    
    fact = 1
        
    while True : 
        if N == 0 :
            break
            
        fact = fact * N
        N -= 1
            
    strN = str(fact)
        
    for i in strN[::-1] :
        if i != '0' : 
            print (' ' * (5-len(str(K))) + f'{K} -> {i}')
            break