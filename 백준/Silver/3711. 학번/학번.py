import sys

N = int(sys.stdin.readline())

for i in range (N) :
    G = int(sys.stdin.readline())
    
    lst = []
    
    for j in range (G) :
        sid = int(sys.stdin.readline())
        lst.append (sid)
        
    m = 1
    
    if G != 1 :
        while True :
            m += 1
            t = 0
            rest = set()
            
            for k in lst :
                l = k % m
                
                if l in rest :
                    t = 1 
                    break
                
                else :
                    rest.add(l)
                
            if t == 1 :
                pass
            
            else :
                break
            
        print (m)
        
    else :
        print (1)