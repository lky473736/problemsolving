import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Q = list(map(int, sys.stdin.readline().split()))

setP = set(P)
rst = [0 for i in range (M)]

for i in range (M) : 
    if Q[i] in setP :
        rst[i] = 1
        
    else :
        pass
    
print (*rst)