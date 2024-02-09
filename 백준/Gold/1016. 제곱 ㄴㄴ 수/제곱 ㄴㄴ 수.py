'''import sys
import math

def eratosthenes (M, N) :
    nums = [0 for i in range (N + 1)]
    nums.insert(0, 1)

    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1

    return nums[M : ]
    
mina, maxa = map(int, sys.stdin.readline().split())

prime = eratosthenes(1, maxa)[:-1]
prime = [idx+1 for idx in range (1, maxa) if prime[idx] == 0]
prime_set = set(prime)
prime_len = len(prime_set)

counting = 0

for i in range (mina, maxa+1) :
    val = i
    factors = set()
    prime_dict = {i : 0 for i in prime}
    j = 0
    
    if val == 1 or val in prime_set : # 1 or 소수
        print (val)
        counting += 1
        continue
    
    while True : # 합성수일 때
        if val in prime_set or j >= prime_len :
            break
        
        if val % prime[j] == 0 :
            c = 0
            
            while val % prime[j] == 0 :
                val = val // prime[j]
                factors.add (prime[j])
                c += 1
            
            factors.add (prime[j])
            prime_dict[prime[j]] += c
            
            j = 0
            c = 0
            
        else :
            j += 1
            
    if val != 1 :
        prime_dict[val] += 1
    
    factors.add (val)
    print (i, "|", factors)
    print (prime_dict)
    
    if len(factors) != 1 :
        print (i, "is no-num")
        counting += 1
        
    token = 0
    
    for i in set(prime_dict.values()) : 
        if i == 0 : 
            pass
        
        elif i != 0 and i % 2 == 0 :
            pass
        
        else :
            token = 1
            break
        
    if token == 1 :
        print (i, "is no-num")
        counting += 1

print (counting)'''

# 문제를 똑바로 읽자

import math
import sys

mina, maxa = map(int, sys.stdin.readline().split())
list_num = [1 for i in range(maxa-mina+1)]
counting = 0
i = 2

while i**2 <= maxa :
    mul = mina // i**2
    
    while mul * (i**2) <= maxa :
        if mul * (i**2) - mina >= 0 and mul * (i**2) - mina <= maxa - mina :
            list_num[mul * (i**2) - mina] = 0
            
        mul += 1
        
    i += 1

print (sum(list_num))