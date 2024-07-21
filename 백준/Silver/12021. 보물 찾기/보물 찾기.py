import sys
import time

a, b = map(int, sys.stdin.readline().split())
xnn, ynn = a, b
prev_xnn, prev_ynn = a, b

while True : 
    # time.sleep(1)
    xnn = (prev_xnn + prev_ynn) / 2
    ynn = 2 * (prev_xnn * prev_ynn) / (prev_xnn + prev_ynn)
    
    # print (xnn, ynn)
    
    if prev_xnn == xnn and prev_ynn == ynn : 
        break
    
    else : 
        prev_xnn = xnn
        prev_ynn = ynn

        
print (xnn, ynn)