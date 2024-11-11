import sys

formula = sys.stdin.readline().rstrip()

if formula[0] == 'x' : 
    print (1)
    
elif formula.find('x') == -1 : 
    print (0)
    
else :
    if formula[0] == '-' and formula[1] == 'x' :
        print (-1)
        
    else : 
        # if formula[0] == '-' and formula[1] != 'x' : 
        #     print (formula[0:2])
        
        # else : 
        #     
        print (formula[0:formula.index('x')])
