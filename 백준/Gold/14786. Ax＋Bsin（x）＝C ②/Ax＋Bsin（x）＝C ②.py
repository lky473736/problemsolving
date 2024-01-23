import sys
import math
import decimal

def sin(x):
    # Adjust the angle to a smaller range to prevent overflow
    x %= 2 * math.pi
    
    decimal.getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    
    return +s

def f(x, A, B, C):
    return A * x + B * sin(x) - C

A, B, C = map(int, sys.stdin.readline().split())

tol = 10**(-9)
start, end = 0, 10**5

while True :
    mid = (start + end) / 2.0
    
    if abs(start - end) < tol :
        break
    
    if f(mid, A, B, C) <= 0 :
        start = mid
        
    else :
        end = mid

print (mid)