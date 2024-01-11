import sys
import math 
import itertools

def eratosthenes (M, N) :
    nums = [0 for i in range (N + 1)]
    
    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums[1:]

N = int(sys.stdin.readline())

if N == 1 or N == 2 or N == 3 or N == 4 or N == 5 or N == 6 or N == 7 :
    print(-1)
    exit()

prime = eratosthenes(1, N)
prime = [index+1 for index in range(N) if prime[index] == 0]
prime.pop(0)

combi_prime = itertools.combinations(prime, 4)

for i in combi_prime :
    if sum(i) == N : 
        break
    
for compo in i : 
    print(compo, end = ' ')



###################################



import sys
import math 
import itertools

def eratosthenes (M, N) :
    nums = [0 for i in range (N + 1)]
    
    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums[1:]
    
T = int(sys.stdin.readline())

prime = eratosthenes(1, 10000)
prime[0] = 1

for i in range (T) :
    n = int(sys.stdin.readline())
    
    nprime = prime[:n].copy()
    nprime = [index+1 for index in range(n) if nprime[index] == 0]

    combi_repla = itertools.combinations_with_replacement(nprime, 2)
    
    list_for_sort = []
    
    for j in combi_repla : 
        if sum(j) == n : 
            list_for_sort.append([j, abs(j[0]-j[1])])
            
    list_for_sort.sort(key = lambda x : x[1])
    
    print (list_for_sort[0][0][0], list_for_sort[0][0][1])
