import sys
import math

def euclidean(X, Y):
    if Y == 0:
        return X

    a = max(X, Y)
    b = min(X, Y)
    p = 0

    if b == 0:
        return a

    while True:
        p = a % b

        if p == 0:
            break

        a = b
        b = p

    return b
    
def eratosthenes (N) :
    nums = [0 for i in range (N + 1)]
    
    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums
    
prime = eratosthenes(1000000)
prime[0] = 1 
prime[1] = 1

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
nprime = [index for index in range(max(A)+1) if prime[index] == 0]
nprime = set(nprime)

gcd = 1
product = 1
set_compo = set()

for compo in A : 
    if compo in nprime : 
        gcd = euclidean(gcd, compo)
        
        if compo in set_compo :
            pass
        
        else :
            product *= compo
            set_compo.add(compo)
        
    else :
        N -= 1
        
if N == 0 :
    print (-1)
    exit()

else :
    print (product // gcd)