'''
LCM(a, b, c) >> LCM(LCM(a, b), c)
LCM(a, b, c) = L
'''

import sys

def euclidean (X, Y) :
    a = Y 
    b = X % Y 
    p = 0
    
    if b == 0 :
        return a
    
    while True :
        p = a % b
        
        if p == 0 :
            break
        
        a = b
        b = p
        
    return b
    
def find_factors (L) : 
    lst = []
    counting = 0
    
    for i in range(1, int(L**0.5) + 1) :
        if L % i == 0 :
            lst.append (i)
            lst.append (L // i)
            counting += 2
            
    return lst, counting

a, b, L = map(int, sys.stdin.readline().split())
LCM_ab = (a*b) // euclidean(a, b)
factors, counting_factors = find_factors(L)
factors = sorted(factors)

# print (LCM_ab)
# print (factors)

if LCM_ab == L :
    print (1)

elif L % a != 0 or L % b != 0 :
    print (-1)
    
else :
    i = 0
    
    while i < counting_factors :
        # print (factors[i])
        if (LCM_ab * factors[i]) // euclidean(LCM_ab, factors[i]) == L :
            print (factors[i])
            break
            
        i += 1