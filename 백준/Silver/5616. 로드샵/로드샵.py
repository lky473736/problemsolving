import sys
sys.setrecursionlimit(10**8)

def factorial (n) : 
    if n == 0 : 
        return 1
        
    else :
        return n * factorial(n-1)

n, m, r = map(int, sys.stdin.readline().split())

if r-n*m < 0 :
    print (0)

else :
    print (factorial(n+r-n*m-1)//(factorial(n-1) * factorial(r-n*m)))