''' O(n^3)
import sys
import math
import itertools 
from functools import reduce

def eratosthenes (M, N) : # 0은 소수, 1은 합성수
    nums = [0 for i in range (N + 1)]
    nums.insert(0, 1)
    
    for i in range (2, int(math.sqrt(N) + 1)) : 
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums[M : -1]

T = int(sys.stdin.readline())

prime = eratosthenes(1, 1000000) # 소수

for _ in range (T) :
    N = int(sys.stdin.readline())
    
    all_suma = 0
    
    for k in range (1, N + 1) : 
        print (k)
        
        prime_factors = set() # 소인수
        suma = 0
        
        if k == 1 : # k가 1이면
            all_suma += 1
            continue
        
        if prime[k-1] == 0 : # k가 소수이면
            all_suma += 1 + k
            continue
        
        for i in range (2, k) : 
            if prime[i-1] == 0 and k % i == 0 :
                prime_factors.add(i)
    
        list_prime_factors_for_factors = [1]
        
        for i in prime_factors :
            while k % i == 0 and k != 1 : 
                k = k // i
                list_prime_factors_for_factors.append(i)
                
        for i in itertools.combinations(list_prime_factors_for_factors, len(list_prime_factors_for_factors)) : 
            print (i)
            suma += reduce(lambda x, y : x*y, i)
            
        all_suma += suma
        print ("-----")
        
    print (all_suma)'''

# DP

import sys

MAX = 1000000

dp = [1] * (MAX + 1)

s = [0] * (MAX + 1)

for i in range(2, MAX+1):
    j = 1
    while i * j <= MAX:
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
    s[i] = s[i-1] + dp[i]

T = int(sys.stdin.readline())
ans = []

for _ in range (T) :
    N = int(sys.stdin.readline())
    ans.append(s[N])
    
print('\n'.join(map(str, ans)) + '\n')