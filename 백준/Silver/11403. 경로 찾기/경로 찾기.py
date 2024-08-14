import sys

N = int(sys.stdin.readline())
mapping = []

for i in range (N) :
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    mapping.append (row)
     
for i in range (N) : # i를 기준으로
    for j in range (N) : # j에서
        for k in range (N) : # k로 가는 정점 존재?
            if mapping[j][i] == 1 and mapping[i][k] == 1 : 
                # j->i, i->k가 있으면 j->k도 있다 (삼단논법)
                mapping[j][k] = 1
                
for row in mapping :
    print (*row)
    
'''
0 1 0
0 0 1
1 0 0

예를 들어서 (2, 1, 1)이라 할때, mapping[j][i]는 1, mapping[i][k]는 1이니 
mapping[j][k]도 1이 됨
'''
