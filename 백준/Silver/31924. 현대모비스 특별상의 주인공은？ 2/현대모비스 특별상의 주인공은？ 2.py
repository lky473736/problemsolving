import sys

N = int(sys.stdin.readline())
matrix = []

for i in range (N) :
    row = list(sys.stdin.readline().rstrip())
    matrix.append(row)
    
cnt = 0
    
# row
# print ('row')
for i in range (N) :
    for j in range (N-4) :
        word = ''.join(matrix[i][j:j+5])
        # print (i, j, word)
        
        if word == 'MOBIS' :
            cnt += 1
    
        elif word == 'SIBOM' :
            cnt += 1
            
# col
# print ('col')
for i in range (N) :
    for j in range (N-4) :
        word = ''.join([matrix[k][i] for k in range (j, j+5)])
        # print (i, j, word)
        
        if word == 'MOBIS' :
            cnt += 1
    
        elif word == 'SIBOM' :
            cnt += 1
      
# diagonal      
# top-left to bottom-right
# print ('diagonal 1')
for i in range (N - 4) :
    for j in range(N - 4) :
        word = ''.join(matrix[i + k][j + k] for k in range(5))
        # print (i, j, word)
            
        if word == 'MOBIS' :
            cnt += 1
        
        elif word == 'SIBOM' :
            cnt += 1

# bottom-left to top-right
# print ('diagonal 2')
for i in range (4, N) :
    for j in range(N - 4):
        word = ''.join(matrix[i - k][j + k] for k in range(5))
        # print (i, j, word)
        
        if word == 'MOBIS' :
            cnt += 1
        
        elif word == 'SIBOM' :
            cnt += 1
            
print (cnt)