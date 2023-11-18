# multiply between matrix

mat1 = list()
mat2 = list()

N, M = map(int, input().split())

for _ in range (N) :
    row = list(map(int, input().split()))
    mat1.append(row)
    
M2, K = map(int, input().split())

for _ in range (M2) :
    row = list(map(int, input().split()))
    mat2.append (row)
    
for n in range (N) : 
    for k in range (K) : 
        suma = 0
        
        for m in range (M) :
            suma += mat1[n][m] * mat2[m][k]
        
        print (suma, end = ' ')
        
    print ()