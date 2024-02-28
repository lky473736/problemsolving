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

prime = eratosthenes(1, 100000)[:-1]
prime = [idx+1 for idx in range (1, 100000) if prime[idx] == 0]
prime_set = set(prime)

N = int(sys.stdin.readline())

for _ in range (N) : 
    K = int(sys.stdin.readline())
    
    dicti = dict()
    i = 0
    
    while True :
        if K % prime[i] == 0 and K != 1 :
            try :
                dicti[prime[i]] += 1
                
            except KeyError :
                dicti[prime[i]] = 1
                
            K = K // prime[i]
                
        else :
            if K == 1 :
                break
            
            i += 1 
    
    for i in dicti.keys() :
        print (i, dicti[i])