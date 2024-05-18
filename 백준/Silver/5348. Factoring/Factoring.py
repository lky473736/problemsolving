
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
lst = []

for i in range (N) :
    lst.append (int(sys.stdin.readline()))

for i in lst :
    ori = i
    factors = []
    
    while i > 1 :
        factors.append(str(prime[i]))
        i = i // prime[i]
    
    if ori == int(factors[0]) : 
        print (f'{factors[-1]}: prime')
        continue
        
    print (f'{ori}:', " ".join(factors))