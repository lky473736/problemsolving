import sys
import math

''' 메모리 초과
def eratosthenes (M, N) :
    nums = [0 for i in range (N + 1)]
    nums.insert(0, 1)
    
    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums[M : ]

prime = eratosthenes(1, 20,000,000)[:-1]
prime_lst = [idx+1 for idx in range (1, 20,000,000) if prime[idx] == 0]
prime_set = set(prime_lst)

c1, c2, c3, c4, c5, c6 = map(int, sys.stdin.readline().split())

# initialization
x1, x2, x3, x4, x5, x6, x7, x8 = 0, 0, 0, 0, 0, 0, 0, 0

for x1 in prime_lst :
    x2 = c1 // x1
    
    if x2 in prime_set :
        x3 = c5 // x2
        
        if x3 in prime_set :
            break
        
        else :
            continue
        
    else :
        continue
    
for x5 in prime_lst :
    x6 = c6 // x5
    
    if x6 in prime_set :
        x7 = c3 // x6
        
        if x7 in prime_set :
            break
        
        else :
            continue
        
    else :
        continue

print (x1, x2, x3, x5, x6, x7)'''

# gcd
def euclidean (X, Y) :
    a = Y 
    b = X % Y 
    p = 0
    
    if b == 0 :
        return a
    
    while True :
        p = a % b
        
        if p == 0 :
            break
        
        a = b
        b = p
        
    return b

c1, c2, c3, c4, c5, c6 = map(int, sys.stdin.readline().split())

x1, x2, x3, x5, x6, x7 = 0, 0, 0, 0, 0, 0

x2 = euclidean(c1, c5)
x1 = c1 // x2
x3 = c5 // x2

x6 = euclidean(c3, c6)
x7 = c3 // x6
x5 = c6 // x6

print (x1, x2, x3, x5, x6, x7)