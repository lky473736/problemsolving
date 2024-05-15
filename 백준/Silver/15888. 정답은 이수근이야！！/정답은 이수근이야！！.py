import sys
import math

def finder (x) :
    while True : 
        if x == 1 and x == int(x) :
            return 1 
            
        elif x < 1 and x != int(x) :
            return 0
            
        x = x / 2

A, B, C = map(int, sys.stdin.readline().split())
determinant = B**2 - 4*A*C

if determinant > 0 : 
    x1 = (-1*B + math.sqrt(determinant)) / (2*A)
    x2 = (-1*B - math.sqrt(determinant)) / (2*A)
    
    if x1 == int(x1) and x2 == int(x2) :
        if x1 > 0 and x2 > 0 : 
            if x1 != 1 and x2 != 1 :
                if finder(x1) == 1 and finder(x2) == 1 :
                    print ("이수근")
                    
                else : 
                    print ("정수근")
                    
            else : 
                print ("정수근")
            
        else :
            print ("정수근")
        
    else :
        print ("둘다틀렸근")
    
else : 
    print ("둘다틀렸근")