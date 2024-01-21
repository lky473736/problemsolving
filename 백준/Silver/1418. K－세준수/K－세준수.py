'''# out of condition

import sys
import math

def eratosthenes (M, N) : # 0은 소수, 1은 합성수
    nums = [0 for i in range (N + 1)]
    nums.insert(0, 1)
    
    for i in range (2, int(math.sqrt(N) + 1)) : 
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums[M : ]
    
prime = eratosthenes(1, 100000)[:-1]
prime = [idx+1 for idx in range (1, 100000) if prime[idx] == 0]
prime = set(prime) # hash

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

counting = 0

key = -1

for i in range (N) : 
    if N - i in prime : # prime
        if N - i <= K :
            counting += 1
        
    else : # non-prime
        for j in range (N - i) :
            if (N - i - j) in prime :
                if (N - i) % (N - i - j) == 0  :
                    key = (N - i - j) # prime-factor (max)
                    
                    if key <= K :
                        counting += 1
                    
                    break
                
print (counting+1)'''

import sys
import math

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

counting = 0

for i in range (2, N + 1) :
    X = i
    
    for Y in range (2, K + 1) :
        while X % Y == 0 :
            X //= Y
            
    if X == 1 : 
        counting += 1
        
print (counting+1)