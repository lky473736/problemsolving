# solve = []
# coefficient = []
# length = 0

# for i in range (N) :
#     line = list(map(int, sys.stdin.readline().rstrip().split()))
#     coefficient.append (line)

# length = len(coefficient[0])

# while True : 
#     token = 0
    
#     for i in range (N) :
#         for j in range (length) :
#             if coefficient[0] == 
        
#         if divider != 1 :
#             for j in range (length) :
#                 coefficient[i][j] = coefficient / divider
                
#         else : 
#             pass
        
#     if token == 0 : 

import sys

N = int(sys.stdin.readline())

solve = [] 
coefficient = []
length = 0

for i in range (N) :
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    coefficient.append(line)

length = len(coefficient[0]) 

for i in range (N) :
    divider = coefficient[i][i] # diagonal == 1
    
    for j in range (i, length) : 
        coefficient[i][j] /= divider

    for j in range (N) :
        if i == j :
            pass
        
        else : 
            factor = coefficient[j][i] 
            
            for k in range(i, length) :
                coefficient[j][k] -= coefficient[i][k] * factor

for i in range (N) :
    solve.append(coefficient[i][-1])
    print("{:.0f}".format(coefficient[i][-1]), end=' ')

        