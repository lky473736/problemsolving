import sys

N, M = map(int, sys.stdin.readline().split())

solve = list()
dot = list()

for i in range (3 * N) :
    line = input()

    if line[2] == '.' :
        dot.append (i)

    solve.append (line)

correct = []

for i in range (3 * N) :
    if i in dot :
        continue

    else :  
        check = ['' for k in range (M)]
        position = [[] for k in range (M)]
        
        n = 0
        mode = 0

        for j in range (8 * M) :
            if solve[i][j] != '.' and mode == 0 :
                mode = 1
                position[n].append([i, j])

            elif solve[i][j] == '.' and mode == 1 :
                mode = 0
                position[n].append([i, j - 1])
                n += 1

            if solve[i][j] != '.' and mode == 1 :
                check[n] += solve[i][j]
                
        for j in range (3 * N) :
            solve[j] = list(solve[j])
        
        for j in range (M) : 
            formula = check[j]
            formula = check[j][:3] + '==' + check[j][4:]
            
            if eval(formula) == True :
                for k in range (position[j][1][1] - position[j][0][1] + 1) :
                    solve[position[j][1][0] - 1][k + position[j][0][1]] = '*'
                    solve[position[j][1][0] + 1][k + position[j][0][1]] = '*'
                
                solve[position[j][0][0]][position[j][0][1]-1] = '*'
                solve[position[j][1][0]][position[j][1][1]+1] = '*'
                
            else :
                solve[position[j][0][0]-1][position[j][0][1]+2] = '/'
                solve[position[j][0][0]][position[j][0][1]+1] = '/'
                solve[position[j][0][0]+1][position[j][0][1]] = '/'
            
for i in solve : 
    print(''.join(i))
    