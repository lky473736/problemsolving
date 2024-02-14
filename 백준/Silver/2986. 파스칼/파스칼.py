import sys
import math

# n - 자기 자신을 제외한 가장 큰 n의 약수

def eratosthenes(num) :
    if num < 2 :
        return False
        
    for i in range(2, int(math.sqrt(num)) + 1) :
        if num % i == 0 :
            return False
            
    return True

N = int(sys.stdin.readline())

if eratosthenes(N) == True : 
    print (N - 1)

else :    
    '''counter = 0
    i = N - 1
    
    while i >= 1 : 
        counter += 1
        
        if N % i == 0 :
            break
        
        i -= 1'''
        
    if N == 2 :
        print (1)
        
    elif N == 1 :
        print (0)
        
    else :
        for i in range(2, int(math.sqrt(N)) + 1) :
            if N % i == 0 :
                break
            
        print (N - N//i)