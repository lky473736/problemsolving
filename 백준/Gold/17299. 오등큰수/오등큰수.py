import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
count_A = dict()

for i in A :
    try : 
        count_A[i] += 1
        
    except : 
        count_A[i] = 1

stack = []
rst = [-1] * N

for i in range (N) : 
    while stack and count_A[A[stack[-1]]] < count_A[A[i]] : 
        rst[stack.pop()] = A[i]
    stack.append(i)

print(*rst)