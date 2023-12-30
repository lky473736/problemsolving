'''N, L = map(int, input().split())
water = list(map(int, input().split()))

water.sort()

temp = water.copy()

position = 0.5
tempposi = position
tape = 0

debug1 = []
debug2 = []

while position <= water[-1] : 
    compo = []
    
    position += 1
    
    for i in range (N) : 
        if position - L <= water[i] <= position : 
            if water[i] in temp :
                compo.append(water[i])
            
    debug1.append(compo)
    
    
while tempposi <= water[-1] : 
    compo = []
    
    tempposi += L
    
    for i in range (N) : 
        if tempposi - L <= water[i] <= tempposi : 
            if water[i] in temp :
                compo.append(water[i])
            
    debug2.append(compo)

    
print (debug1)
print (debug2)

if len(debug1) > len(debug2) : 
    print (len(debug2))
    
else :
    print (len(debug1))
'''

import sys

N, L = map(int, sys.stdin.readline().split())
water = list(map(int, sys.stdin.readline().split()))
water.sort()

count = 0
start = 0

for hole in water :
    if start < hole:
        start = hole + L - 1
        count += 1
        
print (count)