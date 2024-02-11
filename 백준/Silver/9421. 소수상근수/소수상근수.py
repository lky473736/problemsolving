import math
import sys
import time

def eratosthenes (M, N) :
    nums = [0 for i in range (N + 1)]
    nums.insert(0, 1)

    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1

    return nums[M : ]
  
n = int(sys.stdin.readline())  
prime = eratosthenes(1, n)[:-1]
prime = [idx+1 for idx in range (1, n) if prime[idx] == 0]

for i in prime : 
    lst = [i]
    counting = 1
    
    while True :
        suma = 0
        
        for j in str(lst[-1]) : 
            suma += int(j) ** 2
            
        lst.append (suma)
        counting += 1
        
        if lst[-1] == 1 : 
            print (i)
            break
        
        elif lst[-1] in set(lst[1:-1]) : 
            break