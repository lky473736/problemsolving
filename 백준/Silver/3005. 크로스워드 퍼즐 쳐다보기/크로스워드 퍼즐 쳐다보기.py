import sys

R, C = map(int, sys.stdin.readline().split())

crossword = []

for i in range (R) : 
    compo = sys.stdin.readline().rstrip()
    crossword.append(compo)
    
word = []

for counting in range (2) : 
    for i in crossword : 
        if '#' not in i : 
            word.append(i)
        
        else :
            seperate = i.split('#')
            
            for j in seperate : 
                if len(j) >= 2 :
                    word.append(j)
                    
    if counting == 1 : 
        break
    
    crossword = [''.join(str(crossword[j][i]) for j in range(R)) for i in range(C)]

word.sort(key = lambda x : (x, len(x)))
print (word[0])