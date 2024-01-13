import sys

def euclidean (X, Y) :
    a = Y 
    b = X % Y 
    p = 0
    
    if b == 0 :
        return a
    
    while True :
        p = a % b
        
        if p == 0 :
            break
        
        a = b
        b = p
        
    return b
    
N = int(sys.stdin.readline())
list_A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
list_B = list(map(int, sys.stdin.readline().split()))

A, B = 1, 1

for i in range (N) : 
    A *= list_A[i]
    
for i in range (M) : 
    B *= list_B[i]
    
GCD = euclidean(A, B)

if len(str(GCD)) < 9 :
    print (GCD)
    
else :
    print (str(GCD)[-9:])