import sys

N = int(sys.stdin.readline())

position = []

for _ in range (N) :
    x, y = map(int, sys.stdin.readline().split())
    position.append ([x, y])
    
iteration = 0
rst = 0
    
while iteration != N-1 :
    rst += position[iteration][0] * position[iteration+1][1] - position[iteration+1][0] * position[iteration][1]
     
    iteration += 1    
    
rst += position[iteration][0] * position[0][1] - position[0][0] * position[iteration][1]
       
print (round(abs(0.5 * rst), 2))