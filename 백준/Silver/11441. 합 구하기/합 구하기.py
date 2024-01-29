import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

sums = list()
suma = 0

for i in nums :
    suma += i 
    sums.append(suma)

for _ in range (M) : 
    i, j = map(int, sys.stdin.readline().split())
    
    if i == 1 :
        print (sums[j-1])
        
    elif i == j :
        print (nums[j-1])
        
    else :
        print (sums[j-1] - sums[i-2])