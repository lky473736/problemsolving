N, M = input().split()

N = int(N)
M = int(M)

A_component = []
B_component = []

for j in range (N) :
    A_row = list(map(int, input().split()))
    A_component.append (A_row)
        
for k in range (N) :
    B_row = list(map(int, input().split()))
    B_component.append (B_row)

for l in range (N) :
    for p in range (M) :
        summation = A_component[l][p] + B_component[l][p]
        print (summation, end = ' ')
    
    print ()
