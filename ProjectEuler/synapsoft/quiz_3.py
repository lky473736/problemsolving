import sys
import math

position_list = list()

while True : 
    cur = list(map(int, sys.stdin.readline().split()))
    if cur == [0, 0, 0, 0] :
        break
    
    else : 
        position_list.append (cur)
        
print (position_list)
        
# mapping = [[0 for i in range (1, 1922)] for j in range (1, 1082)]
position_set = set()
rst = 0

for position in position_list : 
    for i in range (position[0], position[2]+1) :
        for j in range (position[1], position[3]+1) :
            if (i, j) in position_set : 
                pass
            
            else : 
                position_set.add((i, j))
                # mapping[i][j] = 1
                rst += 1

# print (mapping)
print (rst)
