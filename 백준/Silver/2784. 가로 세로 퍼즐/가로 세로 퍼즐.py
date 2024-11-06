import sys
import itertools

words = []

for i in range (6) : 
    compo = sys.stdin.readline().rstrip()
    words.append (compo)
    
# print (words)
    
permu = list(itertools.permutations(words, 3))
#  print (permu)
token = 0

for i in range (120) : # len (permu)
    puzzle = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    ishere = dict()
    
    for key in words : 
        try : 
            ishere[key] += 1
        except :
            ishere[key] = 1
            
    for j in range (3) :
        for k in range (3)  : 
            puzzle[j][k] = permu[i][j][k]
        
        ishere[permu[i][j]] -= 1
        
    seta = set(words)
    err_token = 0
    for j in range (3) :
        word = puzzle[0][j] + puzzle[1][j] + puzzle[2][j]

        if word not in seta : 
            err_token = 1
            break
        
        if ishere[word] > 0 : 
            ishere[word] -= 1
        
    if err_token == 1 : 
        continue
    
    else : 
        if set(list(ishere.values())) == set([0]) :
            for r in range (3) :
                for c in range (3) :
                    print (puzzle[r][c], end='')
                    
                print ('', end='\n')
                
            token = 1
            break
    
if token != 1 : 
    print (0)
    
