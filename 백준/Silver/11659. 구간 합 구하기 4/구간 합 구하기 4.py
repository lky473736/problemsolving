# https://jow1025.tistory.com/47
# using prefix sum

import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
prefixsum = [num[0]]

for i in range (1, N) :
    prefixsum.append (num[i] + prefixsum[i - 1])

for k in range (M) : 
    i, j = map(int, sys.stdin.readline().split())
    if i - 2 < 0 :
        print (prefixsum[j - 1])
    else :
        print (prefixsum[j - 1] - prefixsum[i - 2])