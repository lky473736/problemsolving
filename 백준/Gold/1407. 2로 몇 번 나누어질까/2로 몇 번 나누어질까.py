import sys

A, B = map(int, sys.stdin.readline().split())

def func (num) :
    cnt = num
    i = 2
    
    while i <= num :
        cnt += (num//i)*(i//2)
        i *= 2
    return cnt

print (func(B) - func(A-1))