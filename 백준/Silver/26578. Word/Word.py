import sys

n = int(sys.stdin.readline())

def linearSearch (arr, size) :
    counting_def = 0
    
    for x in range (size - 4 + 1) :
        if arr[x:x+4] == 'word' or arr[x:x+4] == 'drow' :
            counting_def += 1

    return counting_def
            

for i in range (n) :
    r, c = map(int, sys.stdin.readline().split())
    
    counting = 0
    
    tupls = []
    
    for j in range (r) : 
        tupl = sys.stdin.readline().rstrip()
        
        counting += linearSearch(tupl, c)
            
        tupls.append(tupl)
        
    for j in range (c) : 
        joinCol = ''.join([tupls[k][j] for k in range (r)])
        
        counting += linearSearch(joinCol, r)
    
    positivePoint = [[a, c-1] for a in range (r)] + [[0, a] for a in range (c-1)]
    negativePoint = [[a, 0] for a in range (r)] + [[0, a] for a in range (1, c)]

    for point in positivePoint :
        p = 0
        q = 0
        string = ""
        
        while True :
            string += tupls[point[0]+p][point[1]-q]
            p += 1 
            q += 1
              
            if point[0]+p == r or point[1]-q < 0 :
                if len(string) >= 4 :
                    counting += linearSearch(string, len(string))
                        
                else :
                    pass
                    
                break
    
    for point in negativePoint :
        p = 0
        q = 0
        string = ""
        
        while True :
            string += tupls[point[0]+p][point[1]+q]
            p += 1 
            q += 1
                
            if point[1]+q >= r or point[0]+p >= c :
                if len(string) >= 4 :
                    counting += linearSearch(string, len(string))
                    
                else :
                    pass
                
                break
    
    print (counting)