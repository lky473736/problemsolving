import sys
import math

# def eratosthenes (M, N) :
#     nums = [0 for i in range (N + 1)]
#     nums.insert(0, 1)

#     for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
#         if nums[i] == 0 :
#             for j in range (i + i, N + 1, i) :
#                 nums[j] = 1

#     return nums[M : ]

# prime = eratosthenes(1, 10**9)[:-1]
# prime = [idx+1 for idx in range (1, 10**9) if prime[idx] == 0]
# prime_set = set(prime)

N = int(sys.stdin.readline())
Xlist = map(int, sys.stdin.readline().split())

for X in Xlist :
    if int(math.sqrt(X)) ** 2 == X :
        print (1, end=' ')
        
    else : 
        print (0, end=' ')