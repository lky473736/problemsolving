import sys

t = int(sys.stdin.readline())

for _ in range (t) : 
    n = int(sys.stdin.readline())
    
    clothes = dict()
    
    for i in range (n) : 
        name, sort = sys.stdin.readline().rstrip().split()
        
        if sort in clothes.keys() :
            clothes[sort].append(name)
        
        else : 
            clothes[sort] = [name]
            
    list_length = [len(compo) for compo in clothes.values()]
   
    counting = 1
    
    for k in list_length : 
        counting *= (k + 1)
        
    counting -= 1
    
    print (counting)