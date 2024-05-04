import sys
import math

P = int(sys.stdin.readline())

def divide_numbers(dividend, divisor, limit) :
    if divisor == 0 :
        return 0

    quotient = 0
    remainder = dividend

    while remainder >= divisor :
        remainder -= divisor
        quotient += 1

    return quotient, remainder

for i in range (P) :
    equation = sys.stdin.readline().rstrip()
    
    a, b, c = "", "", ""
    ind = 0
    mode = 0
    start = 0
    
    while True : 
        if mode == 0 :
            if equation[ind] == 'x' :
                mode = 1
            else :   
                a += equation[ind]
            
        elif mode == 1 : 
            if equation[ind] in [' ', '+'] :
                if start != 0 :
                    b = equation[start:ind]
                    start = 0
                    mode = 2
            
            else : 
                if start == 0 :
                    start = ind
                
        elif mode == 2 : 
            if equation[ind] in [' ', '='] :
                pass
            
            else : 
                c = equation[ind:]
                break
            
        ind += 1
        
    # print (a, b, c)
    
    a, b, c = int(a), int(b), int(c)
    
    print (f"Equation {i+1}")
    
    if a == 0 :
        if b - c == 0 :
            print ("More than one solution.")
            
        else : 
            print ("No solution.")
        
    else : 
        rst = str((c-b)/a)
        # print (rst)
        
        ind = 0 
        integer = 0
        decimal = 0
        
        i = 0
        
        while True :
            if rst[i] == '.' :
                integer = rst[:i]
                break
            
            i += 1
        
        try : 
            decimal = rst[i+1:]
            
        except : 
            pass
        
        # print ("int, dec :", integer, decimal)
        
        if 'e' in decimal : 
            integer = '0'
            decimal = '000000'
        
        else :
            if len(decimal) > 6 : 
                decimal = decimal[:6]
                
            elif len(decimal) < 6 : 
                decimal = decimal + '0' * (6 - len(decimal))
            
        rst = integer + '.' + decimal
        
        print (f"x =", rst)
    
    print ()