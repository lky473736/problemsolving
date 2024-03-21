import sys
 
n = int(sys.stdin.readline())

for i in range (n) :
    m = int(sys.stdin.readline())
    
    dicti = {}
    
    for j in range (m) :
        name, num = map(str, sys.stdin.readline().rstrip().split())
        dicti[name] = int(num)
        
    rst = list(dicti.keys())
    
    rst.sort(key = lambda x : (dicti[x]), reverse = True)
    
    for compo in rst : 
        if compo == rst[-1] :
            print (compo)
            
        else : 
            print (compo + ",", end = ' ')