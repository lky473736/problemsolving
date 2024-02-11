import math
import sys

def eratosthenes (M, N) :
    nums = [0 for i in range (N + 1)]
    nums.insert(0, 1)

    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1

    return nums[M : ]
  
K = int(sys.stdin.readline())  
prime = eratosthenes(1, 500000)[:-1]
prime = [idx+1 for idx in range (1, 500000) if prime[idx] == 0]

print (prime[K-1])