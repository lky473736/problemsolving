def mattimes(mat, cat, N):
    rst = [[0 for _ in range(N)] for _ in range(N)]
    
    for h in range(N):
        for p in range(N):
            findcompo = 0
                
            for q in range(N):
                findcompo += mat[h][q] * cat[q][p]
                
            rst[h][p] = findcompo % 1000
        
    return rst
    
def faster(mat, N, B):
    if B == 1:
        return mat

    matcom = faster(mat, N, B // 2)  # B의 절반을 계산
    
    if B % 2 == 0:
        return mattimes(matcom, matcom, N)
    else:
        return mattimes(mat, mattimes(matcom, matcom, N), N)

import sys

N, B = map(int, sys.stdin.readline().split())

rowlist = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    rowlist.append(row)

result = faster(rowlist, N, B)

for o in range(N):
    for compo in result[o]:
        if compo == 1000 : 
            print (0, end = " ")
            
        else :
            print(compo, end=" ")

    print()

 # A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.