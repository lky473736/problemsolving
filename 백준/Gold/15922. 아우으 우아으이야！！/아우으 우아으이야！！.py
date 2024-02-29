import sys

N = int(sys.stdin.readline())

lines = []

for i in range (N) :
    x, y = map(int, sys.stdin.readline().split())
    
    if i == 0 :
        lines.append ([x, y])
        continue
    
    if lines[-1][0] <= x and lines[-1][1] >= x: 
        if y <= lines[-1][1] :
            pass
        
        else :
            lines[-1][1] = y
            
    else :
        lines.append([x, y])
        
rst = 0

for i in lines :
    rst += abs(i[0] - i[1])
    
print (rst)