import sys
import math

nlist = []
for _ in range (20) :
    line = map(str, sys.stdin.readline().split())
    
    for i in range (20) :
        line[i] = int(line[i])
        
    nlist.append (line)
    
    
rst = []

# horizontal
for i in range (20) :
    ind = 0
    
    while True : 
        if ind+4 > 15 : 
            break
        
        compo = nlist[i][ind:ind+4]
        cur = []
        
        for j in range (4) :
            cur.append(compo[j])
            
        rst.append (cur)
            
        ind += 1

# vertical
for i in range (20) :
    ind = 0 
    
    while True : 
        if ind+4 > 15 : 
            break
        
        compo = [nlist[j][i] for j in range (ind, ind+5)]
        cur = []
        
        for j in range (4) :
            cur.append (compo[j])
            
        rst.append (cur)
            
        ind += 1
        
# diagonal (left)
for i in range (4-1, 21) :
    cur = []
    com = 0
    token = 0
    
    while True : 
        
        rst.append ([nlist[j][com], nlist[j-1][com+1], nlist[j-2][com+2], nlist[i-3][com+3])
        com += 1
