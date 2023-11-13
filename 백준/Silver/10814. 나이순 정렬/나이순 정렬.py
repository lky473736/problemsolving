import sys

input = sys.stdin.readline().rstrip()
N = int(input)

finder = []

for i in range (N) :
    input = sys.stdin.readline().rstrip()
    compo = input
    finder.append ((int(compo.split(' ')[0]), compo.split(' ')[1]))
    
sortedarr = sorted(finder, key = lambda x : x[0])

for j in sortedarr :
    print (j[0], j[1])