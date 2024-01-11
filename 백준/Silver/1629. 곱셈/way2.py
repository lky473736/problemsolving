import sys

A, B, C = map(int, sys.stdin.readline().split())

def power (A, B) :
    result = 1
    
    while B > 0 :
        if B % 2 == 1 :
            result *= A
            
        A *= A
        B //= 2
        
    return result

print (power(A, B) % C)
