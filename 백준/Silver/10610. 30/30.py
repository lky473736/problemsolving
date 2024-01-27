import sys

N = list(sys.stdin.readline().rstrip())

if int(''.join(N)) % 3 == 0 :
    if '0' in N : 
        N.sort(reverse = True)
        
        for i in N :
            print (i, end='')
            
    else :
        print (-1)
    
else :
    print (-1)