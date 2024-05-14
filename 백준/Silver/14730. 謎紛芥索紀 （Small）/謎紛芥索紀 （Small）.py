import sys

N = int(sys.stdin.readline())

rst = 0

for i in range (N) :
    C, K = map(int, sys.stdin.readline().split())
    rst += C * K
    
print (rst)