import sys
import math

def eratosthenes (M, N) :
    nums = [0 for i in range (N + 1)]
    nums.insert(0, 1)
    
    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums[M : ]

prime = eratosthenes(1, 1299709)[:-1]
prime = set([idx+1 for idx in range (1, 1299709) if prime[idx] == 0])

T = int(sys.stdin.readline())

for _ in range (T) : 
    k = int(sys.stdin.readline())
    
    if k not in prime : 
        i = 1
        j = 0
        
        while True :
            if k - i in prime :
                break
            
            i += 1
        
        m = k - i
        i = 0
        
        while True :
            if k + i in prime : 
                break
            
            i += 1
        
        M = k + i
            
        print (M - m)
        
    else :
        print (0)