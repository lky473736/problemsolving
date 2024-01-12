import sys
import math 
import itertools

def eratosthenes (N) :
    nums = [0 for i in range (N + 1)]
    
    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums
    
T = int(sys.stdin.readline())

prime = eratosthenes(10000)
prime[0] = 1
nprime = prime.copy()
nprime = [index for index in range(10000) if nprime[index] == 0]
nprime = set(nprime)

for i in range (T) :
    n = int(sys.stdin.readline())
    
    l = []
    
    for j in range (2, n) : 
        if j in nprime and n - j in nprime :
            l.append((j, abs(j - (n - j))))
    
    l.sort(key = lambda x : x[1])
    
    print (l[0][0], n - (l[0][0]))

    ''' 시간 초과
    combi_repla = itertools.combinations_with_replacement(nprime, 2)
    
    list_for_sort = []
    
    for j in combi_repla : 
        if sum(j) == n : 
            list_for_sort.append([j, abs(j[0]-j[1])])
            
    list_for_sort.sort(key = lambda x : x[1])
    
    print (list_for_sort[0][0][0], list_for_sort[0][0][1])'''