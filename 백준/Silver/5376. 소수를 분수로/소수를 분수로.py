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

T = int(sys.stdin.readline())

for i in range (T) :
    decimal = sys.stdin.readline().rstrip().split('.')[1]
    # print (decimal)
    
    num = ''
    floating = [0, '', '']
    token = 0
    
    cnt = 0
    all_cnt = 0
    
    for char in decimal : 
        if token == 1 : 
            if char == ')' :
                floating[0] = cnt
                break
                
            floating[2] += char
            
            cnt += 1
            all_cnt += 1
            continue
            
        if char == '(' : 
            token = 1
            continue
    
        floating[1] += char
        all_cnt += 1
        
    # print (all_cnt, floating)
    denominator, divider = 0, 0
    if floating[0] == 0 and floating[2] == '' :
        denominator = 10 ** all_cnt
        divider = int(floating[1])
        
    else : 
        denominator = int(floating[0] * '9' + (all_cnt-floating[0]) * '0')
        
        if floating[0] == all_cnt :
            divider = int(floating[2])
        
        else : 
            divider = int(floating[1] + floating[2]) - int(floating[1])
        
    gcd = euclidean (denominator, divider) 
    print (f'{divider//gcd}/{denominator//gcd}')
    
    # for char in decimal :
    #     if char == '.' :
    #         fixing = [cnt, num]
    #         num = ''
    #         cnt = 1
    #         continue
        
    #     elif char == '(' :
    #         if num != '' :
    #             floating.append (num)
                
    #         token = 1
    #         continue
        # num += char
        # cnt += 1