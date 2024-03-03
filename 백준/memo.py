# 구현해야 할 것 
# 1) in 키워드 말고 완전탐색
# 2) 모든 대각선

import sys

n = int(sys.stdin.readline())

for i in range (n) :
    r, c = map(int, sys.stdin.readline().split())
    
    counting = 0
    
    tupls = []
    
    for j in range (r) : 
        tupl = sys.stdin.readline().rstrip()
        
        if 'word' in tupl : 
            counting += 1
            
        if 'drow' in tupl :
            counting += 1
            
        tupls.append(tupl)
        
    # print (tupls)
    
    for j in range (c) : 
        joinCol = ''.join([tupls[k][j] for k in range (r)])
        # print (joinCol)
        
        if 'word' in joinCol : 
            counting += 1
            
        if 'drow' in joinCol :
            counting += 1
            
    diagonalPositive = ''.join([tupls[r-1-j][j] for j in range (r)])
    diagonalNegative = ''.join([tupls[j][j] for j in range (r)])
    # print (diagonalPositive, diagonalNegative)
    
    if 'word' in diagonalPositive :
        counting += 1
        
    if 'drow' in diagonalPositive :
        counting += 1
        
    if 'word' in diagonalNegative :
        counting += 1
        
    if 'drow' in diagonalNegative :
        counting += 1
        
    print (counting)
        
    if sumation(a1, r, counting) == N : 
        break'''
