import sys
import math

mapping = [[0 for j in range (21)] for i in range (21)]
for i in range (21) :
    mapping[i][0] = 1
    mapping[0][i] = 1
    
for i in range (1, 21) : 
    for j in range (1, 21) :
        mapping[i][j] = mapping[i][j-1] + mapping[i-1][j]
        
for i in range (21) :
    for j in range (21) :
        print (mapping[i][j], end = '\t')
        
    print ()
    
print (mapping[20][20])
