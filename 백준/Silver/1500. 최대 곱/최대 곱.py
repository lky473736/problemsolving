# [S//K] * K에 각 요소 S%k개에다 1을 더한 것

import sys

S, K = map(int, sys.stdin.readline().split())

arr = [S//K for i in range (K)]

for i in range (S % K) : 
    arr[i] += 1
    
rst = 1

for j in range (K) :
    rst *= arr[j]
    
print (rst)