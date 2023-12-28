import sys

T = int(sys.stdin.readline())

for _ in range (T) :
    floor, num = map(int, sys.stdin.readline().split())
    
    ind = 0
    i = 0
    rst = 1
    
    while ind != num : 
        a = abs(((floor - 1) - 2 * i))
            
        if ind < ((floor + 1) / 2) - 1 :
            rst += a
                
        else :
            rst -= a
                
        i += 1
        ind += 1
            
    print (rst)