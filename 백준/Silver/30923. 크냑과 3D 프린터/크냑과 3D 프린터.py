import sys

N = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))

sumation = sum(h)
rst = 2 * sumation + 2 * N

for i in range (N) :
    if i == 0 : 
        rst += h[i]
        
    else : 
        if h[i] == h[i-1] :
            pass
        
        else : 
            rst += abs(h[i] - h[i-1])
            
print (rst + h[N-1])