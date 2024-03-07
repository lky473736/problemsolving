import sys
import math

def eratosthenes (M, N) :
    nums = [0 for i in range (N + 1)]
    nums.insert(0, 1)

    for i in range (2, int(math.sqrt(N) + 1)) :
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1

    return nums[M : ]

while True :
    n = int(sys.stdin.readline())
    
    if n == 0 :
        break
    
    prime = eratosthenes(1, 2*n + 1)[:-1]
    prime = [idx for idx in range (n, 2*n) if prime[idx] == 0]
    
    print (len(prime))