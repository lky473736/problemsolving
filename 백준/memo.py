import sys
import math

N = int(sys.stdin.readline())

if N < 7 :
    print (-1)
    exit()

'''while True :
    if suma > N :
        a1 = 1
        r += 1
        
    arr = [a1, a1*r, a1*r*r]
    length_arr = 3
    suma = a1 * (1 + r + r**2)
    
    while True :
        if suma == N :
            break
        
        elif suma > N :
            a1 += 1
            break
            
        arr.append (a1 * r**(length_arr))
        suma += a1 * r**(length_arr)
        length_arr += 1
        
    if suma == N : 
        break'''

def sumation(a1, r, n) :
    return a1 * (r**n - 1) // (r - 1)
        
a1 = 1

while True : 
    if a1 == N : 
        print (-1)
        exit()
    
    for r in range (2, int(math.sqrt(N)) + 1) :
        for counting in range (3, int(math.log(N, r)) + 2) : 
            if sumation(a1, r, counting) == N : 
                print (counting)
                    
                for i in range (counting) : 
                    print (a1*r**i, end = ' ')
                        
                exit()
                    
            elif sumation(a1, r, counting) > N :
                break
            
    a1 += 1

            
    '''while True :
        if sumation(a1, r, 3) > N : 
            break
        
        elif sumation(a1, r, counting) == N :
            break
        
        a1 += 1
        arr.append (a1*r**counting)
        counting += 1
        
    if sumation(a1, r, counting) == N : 
        break'''
