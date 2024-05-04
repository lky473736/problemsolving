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

counting = 0
    
while True : 
    counting += 1
    input_ary = int(sys.stdin.readline())
    
    if input_ary == 0 : 
        break
    
    else :
        arr = []
        
        for i in range (input_ary) :
            compo = sys.stdin.readline().rstrip()
            
            if compo == '1' : 
                arr.append ([1, 1])
                continue
            
            elif compo == '0' :
                arr.append ([0, 1])
                continue
            
            if ',' in compo : # 대분수
                integer_part = []
                    
                j = 0
                    
                for character in compo :
                    if character == ',' :
                        break
                        
                    integer_part.append (character)
                    j += 1
                        
                integer = int(''.join(integer_part))
                    
                numerator_part = []
                    
                j += 1 
                    
                for character in compo[j:] :
                    if character == '/' :
                        break
                        
                    numerator_part.append (character) 
                    j += 1
                
                numerator = int(''.join(numerator_part))
                denominator = int(''.join(compo[j+1:]))
                    
                arr.append ([integer*denominator+numerator, denominator])
                
            else :
                j = 0
                
                for character in compo :
                    if character == '/' :
                        break
                        
                    j += 1
                    
                numerator = int(''.join(compo[:j]))
                denominator = int(''.join(compo[j+1:]))
                        
                arr.append ([numerator, denominator])
                
    # print (arr)
    
    temp = 0
    rst = []
    
    for i in range (input_ary) : 
        if i == 0 :
            temp = arr[i]
            
        else :
            rst = [temp[0]*arr[i][1] + temp[1]*arr[i][0], temp[1] * arr[i][1]]
            temp = rst
            
    # print (rst)
    
    testrst = ""
    
    if rst[0] == rst[1] : 
        testrst = str(1)
        
    else :
        rst = [rst[0] // euclidean(rst[0], rst[1]), rst[1] // euclidean(rst[0], rst[1])]
        
        # print (rst)
        
        if rst[0] > rst[1] :
            integer = str(rst[0] // rst[1]) 
            numerator = str(rst[0] - int(integer)*rst[1])
            denominator = str(rst[1])
            
            # print (integer, numerator, denominator)
            
            if numerator == '0' :
                testrst = integer
                
            else :
                testrst = integer + ',' + numerator + '/' + denominator

        else : 
            # print (rst)
            if rst[0] == 0 :
                testrst = '0'
                
            else : 
                testrst = str(rst[0]) + '/' + str(rst[1])
            
    print (f"Test {counting}:", testrst)