import sys

N = int(sys.stdin.readline())

A = []
B = []

for i in range (N) :
    lst = list(map(int, sys.stdin.readline().split()))
    A.append(lst)
    
for i in range (N) :
    lst = list(map(int, sys.stdin.readline().split()))
    B.append(lst)

C = 0

for i in range (N) :
    for j in range (N) :
        state = 0
        compo = 0
        
        for k in range (N) :
            compo += A[i][k] * B[k][j]
            
        if compo > 0 :
            C += 1
            
print (C)