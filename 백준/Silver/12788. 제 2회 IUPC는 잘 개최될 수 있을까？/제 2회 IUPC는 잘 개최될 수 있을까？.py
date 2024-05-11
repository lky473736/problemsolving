import sys

N = int(sys.stdin.readline())
M, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A = sorted(A, reverse = True)

rest = M * K
counting = 0
i = 0

while True : 
    counting += 1
    
    try : 
        if rest > A[i] : 
            rest -= A[i]
            i += 1
            
        else : 
            print (counting)
            exit()
            
    except IndexError : 
        break
    
print ("STRESS")