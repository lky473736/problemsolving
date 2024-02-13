import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

def dnc(a, b) :
    if b == 0 :
        return 1
        
    x = dnc(a, b // 2) % M

    if b % 2 == 0 :
        return (x ** 2) % M
    
    else :
        return (x ** 2 * a) % M

j = 2
rst = 0

for i in lst :
    rst += dnc(i, j)
    rst %= M
    j += 1

print (rst % M)