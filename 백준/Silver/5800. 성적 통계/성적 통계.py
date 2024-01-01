import sys

K = int(sys.stdin.readline())

score = []
nlist = []

for _ in range (K) :
    scorecompo = list(map(int, sys.stdin.readline().split()))
    nlist.append(scorecompo[0])
    scorecompo.pop(0)
    score.append(sorted(scorecompo))
    
for i in range (K) : 
    gap = sorted([(score[i][j] - score[i][j-1]) for j in range (1, nlist[i])])
    print (f'Class {i+1}')
    print (f'Max {score[i][-1]}, Min {score[i][0]}, Largest gap {gap[-1]}')