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
    
A, B = map(int, sys.stdin.readline().split())

prime = eratosthenes(1, 10000000)[:-1]
prime_lst = [idx+1 for idx in range (1, 10000000) if prime[idx] == 0]

counting = 0
squares = 2

while True :
    if 2 ** squares > B :
        break
    
    for compo in prime_lst :
        if A <= compo ** squares and compo ** squares <= B :
            counting += 1
            
        elif compo ** squares > B :
            break
        
    squares += 1
    
print (counting)