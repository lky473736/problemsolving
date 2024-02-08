'''
    D에 있는 모든 수의 배수 == D에 있는 모든 수의 최소공배수를 구해 1배, 2배...
    M에 있는 모든 수의 약수 == M에 있는 모든 수의 최대공약수의 약수
'''


import sys
import math

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

size_D, size_M = map(int, sys.stdin.readline().split())
D = list(map(int, sys.stdin.readline().split()))
M = list(map(int, sys.stdin.readline().split()))

if 0 in D or 0 in M : # 만약 배열에 0이 들어있다면
    print (0)
    exit()

GCD_D = D[0]
LCM_D = 1

if size_D != 1 : 
    for i in D : 
        GCD_D = euclidean(LCM_D, i)
        LCM_D = (LCM_D * i) // GCD_D 
    
else :
    times_D, GCD_D = D[0], D[0]
    LCM_D = times_D 

GCD_M = M[0]

# way 1 : 시간초과 (50%)
'''if size_M != 1 :
    for i in M : 
        GCD_M = euclidean(i, GCD_M)
        
else :
    GCD_M = M[0]

i = 1

# print (GCD_D, LCM_D, GCD_M)

if int(GCD_M / LCM_D) == GCD_M / LCM_D : 
    counting = 0
    
    while GCD_M >= LCM_D * i : 
        if GCD_M % (LCM_D * i) == 0 :
            counting += 1
            
        else :
            pass
        
        i += 1
        
    print (counting)
    
else :
    print (0)'''
    
# way 2 : 시간초과 (1%)
'''counting = 0
i = 1

while True :
    break_code = 0
    counter = 0
    
    for k in M :
        if i * LCM_D <= k and k % (i * LCM_D) == 0 :
            counter += 1
        
        if k < i * LCM_D :
            break_code = 1
            break
    
    if break_code == 1 :
        print (counting)
        break
    
    elif break_code == 0 and counter == size_M :
        counting += 1
        
    i += 1'''
    
if size_M != 1 :
    for i in M : 
        GCD_M = euclidean(i, GCD_M)
        
else :
    GCD_M = M[0]

counter = GCD_M / LCM_D
rst = set()

if int(counter) == counter : 
    for i in range (1, int(math.sqrt(counter))+1) : 
        if counter % i == 0 :
            rst.add(counter // i)
            rst.add(i)
            
    print (len(rst))
    
else :
    print (0)