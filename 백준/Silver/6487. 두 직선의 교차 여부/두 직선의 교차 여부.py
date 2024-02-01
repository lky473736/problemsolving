import sys

N = int(sys.stdin.readline())

for _ in range (N) : 
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    
    if x1 == x2 and x3 == x4 : 
        if x1 == x3 :
            print ("LINE")
            
        else :
            print ("NONE")
        
        continue
    
    if (y1-y2)*(x3-x4) == (y3-y4)*(x1-x2) : # slope 
        if (x3-x4)*(y1-y2)*(-1*x1) + (x3-x4)*(x1-x2)*y1 == (x1-x2)*(y3-y4)*(-1*x3) + (x1-x2)*(x3-x4)*y3 : # position of y-axis 
            print ("LINE")
            
        else : 
            print ("NONE")
    
    else : # POINT
        px = "{:.2f}".format(float(((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))))
        
        py = "{:.2f}".format(float(((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))))
        
        if px == "-0.00" : 
            px = "0.00"
        
        if py == "-0.00" : 
            py = "0.00"

        print ("POINT", px, py)