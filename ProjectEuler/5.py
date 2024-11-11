import sys
import math

num = 1

# while True : 
#     print (num)
#     token = 0
    
#     for i in range (1, 21) :
#         if num % i == 0 :
#             pass
        
#         else :
#             token = 1
#             break
        
#     if token == 1 : 
#         pass
    
#     else : 
#         print (num)
#         break
    
#     num += 1


# optimization by GCD-LCM way

N = int(sys.stdin.readline())

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
    
cur = 0

for i in range (1, N+1) : 
    if i == 1 : 
        cur = 1 
        
    GCD = euclidean(cur, i)
    LCM = i * cur // GCD
    print (GCD, LCM)
    
    cur = LCM

print (cur)

'''
20
1 1
1 2
1 6
2 12
1 60
6 60
1 420
4 840
3 2520
10 2520
1 27720
12 27720
1 360360
14 360360
15 360360
8 720720
1 12252240
18 12252240
1 232792560
20 232792560
232792560
'''
