import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

for i in range (N) :
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

A = int(input())

# arr = [[arr[i][j] for i in range(M)] for j in range(N)]

rst = [[] for i in range (M)]

for i in range (M) : 
    for j in range (N) :
        rst[i].append (arr[j][i])
        
    rst[i] = sum(rst[i])

sum_part = []

for i in range (M - A + 1) : 
    sum_part.append (sum(rst[i:i+A]))

print (max(sum_part))