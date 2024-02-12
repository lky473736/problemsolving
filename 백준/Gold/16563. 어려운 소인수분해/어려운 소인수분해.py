import sys
import math

def eratosthenes (prime) :
    for i in range(2, 2250) :
        if prime[i] == i :
            for j in range(i*2, 5000001, i) :
                if prime[j] == j : 
                    prime[j] = i

prime = [i for i in range(5000001)]
eratosthenes(prime)

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

for i in lst :
    factors = []
    
    while i > 1 :
        factors.append(str(prime[i]))
        i = i // prime[i]
        
    print (" ".join(factors))
        