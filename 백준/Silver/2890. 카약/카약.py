import sys
import re

R, C = map(int, sys.stdin.readline().split())

score = [[0, i+1] for i in range (R)]

for i in range (R) :
    state = sys.stdin.readline().rstrip()
    
    if state == 'S' + '.' * (C - 2) + 'F' :
        pass
    
    else : 
        numbers = re.findall(r'\d+', state)[0]
        
        position = state.index(numbers)
        
        score[int(numbers[0][0]) - 1][0] = position

ranking = sorted(score, key=lambda x : -x[0])
lenrank = len(ranking)

rst = [0 for i in range (lenrank)]
ranknum = 1

for i in range (lenrank) :
    if i == 0 :
        pass
        
    else :
        if ranking[i][0] == ranking[i-1][0] :
            pass
        
        else :
            ranknum += 1
    
    rst[ranking[i][1] - 1] = ranknum
        
for i in range (9) :
    print (rst[i])