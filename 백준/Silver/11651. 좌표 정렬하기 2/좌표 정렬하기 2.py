import sys

N = int(sys.stdin.readline())
position = []

for _ in range (N) :
    x, y = map(int, sys.stdin.readline().split())
    position.append ([x, y])
    
position.sort (key = lambda x : [x[1], x[0]])

for compo in position : 
    print (compo[0], compo[1])