import sys

N, M = map(int, sys.stdin.readline().split())

pokemon = []

for _ in range (N) :
    mon = sys.stdin.readline().rstrip()
    pokemon.append (mon)
    
for _ in range (M) :
    question = sys.stdin.readline().rstrip()
    
    if question.isdigit() == True :
        print (pokemon[int(question) - 1])
        
    else :
        print (pokemon.index(question) + 1)
    
    