import sys

image = []

R, C = map(int, sys.stdin.readline().split())

for i in range (R) :
    row = list(map(int, sys.stdin.readline().split()))
    image.append (row)
    
T = int(sys.stdin.readline())
    
counting = 0
    
for j in range (R - 2) : 
    for k in range (C - 2) : 
        filter = [image[a][b] for a in range (j, j+3) for b in range (k, k+3)]
        filter.sort()
        
        if filter[4] >= T : 
            counting += 1

print (counting)