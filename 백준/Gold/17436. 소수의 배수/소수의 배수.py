import sys
import math
import itertools

N, M = map(int, sys.stdin.readline().split())
primes = list(map(int, sys.stdin.readline().split()))

'''nums_set = set()

global counting
counting = 0'''

'''def eratosthenes (C, K) :
    global counting
    i = C
    
    if nums[i] == 0 :
        for j in range (i + i, K + 1, i) :
            if nums[j] == 1 :
                pass
            
            else :
                nums[j] = 1
                counting += 1'''

'''for prime in primes : 
    i = 1
    
    while True :
        if prime * i > M : 
            break
        
        if (prime * i) in nums_set : 
            pass
        
        else :
            nums_set.add (prime * i)
            counting += 1
            
        i += 1
    
print (counting)'''

'''counting = 0
current = 0
i = 1

for prime in primes :
    while True :
        if current > M : 
            break
    
    current = prime '''
    
counting = 0
K = 0
operand = []

if N >= 2 :
    '''while True :
        if N - 1 == i : 
            break
        
        counting += M // primes[i]
        counting += M // primes[i+1]
        counting -= M // (primes[i] * primes[i+1])
        
        i += 1'''
        
    while True :
        component_set = []
        divider = 1
        
        if K > N : 
            break
        
        K += 1
        
        if K == 1 or K == N :
            if K == 1 : # 1 
                for c in range (N) : 
                    component_set.append(M // primes[c])
                
            else : # N
                divider = 1
                for c in range (N) :
                    divider = divider * primes[c]
                    
                component_set.append(M // divider)
        
        else :
            '''for c in range (N - K + 1) :
                for d in range (K) :
                    divider *= primes[c+d]

                component_set.append (M // divider)
                divider = 1
                        
            for p in range (K-1) :
                divider *= primes[N-1-p]
                
            divider *= primes[0]
            
            component_set.append(M // divider)'''
            
            combi = itertools.combinations(primes, K)
            
            for compo in combi : 
                divider = 1
                
                for j in compo : 
                    divider *= j
                    
                component_set.append (M // divider)
            
        operand.append (component_set)
        
    operator = '+'
    
    # operand.pop()
    
    for i in operand :
        if operator == '+' :
            operator = '-'
            counting += sum(i)
            
        else :
            operator = '+'
            counting -= sum(i)
        
else :
    counting += M // primes[0]

print (counting)