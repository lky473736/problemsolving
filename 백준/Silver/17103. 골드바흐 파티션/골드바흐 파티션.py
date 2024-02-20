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
    
prime = eratosthenes(1, 1000000)[:-1]
prime = [idx+1 for idx in range (1, 1000000) if prime[idx] == 0]
prime_set = set(prime)

T = int(sys.stdin.readline())

for _ in range (T) :
    N = int(sys.stdin.readline())
    
    counting = 0
    
    for i in range (2, N // 2 + 1) : 
        if i in prime_set and N - i in prime_set :
            counting += 1
            
    print (counting)
