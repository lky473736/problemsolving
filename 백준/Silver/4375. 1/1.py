# https://stackoverflow.com/questions/37133547/time-complexity-of-string-concatenation-in-python

import sys

while True : 
    try : 
        n = int(sys.stdin.readline().rstrip())
        
    except :
        break
    
    i = ['1']
    counting = 1
    
    while True :
        if int(''.join(i)) % n == 0 :
            break
        
        i.append('1')
        counting += 1
        
    print (counting)