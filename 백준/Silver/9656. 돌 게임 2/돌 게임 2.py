import sys

N = int(sys.stdin.readline())

'''if N < 4 : 
    if N == 1 or N == 3 :
        print ('CY')
        
    elif N == 2 :
        print ('SK')

else :
    while N != 3 : 
        N -= 1
        
        if state == 'CY' : 
            state = 'SK'
        
        else :
            state = 'CY'
            
    if state == 'CY' : 
        state = 'SK'
        
    else :
        state = 'CY' '''

if N % 2 != 0 :
    print ("CY")
    
else :
    print ("SK")