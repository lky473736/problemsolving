# eratosthenes's filter for finding prime
# https://velog.io/@max9106/Algorithm-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4

import math 

M, N = map(int, input().split())

def eratosthenes (M, N) :
    nums = [0 for i in range (N + 1)]
    
    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums[M : ]

finder = eratosthenes(M, N)

for i in range (len(finder)) :
    if finder[i] == 0 and i + M != 1:
        print (i + M)
        