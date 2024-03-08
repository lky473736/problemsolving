import sys

N, M = map(int, sys.stdin.readline().split())

seta = set()

for _ in range (N) :
    seta.add(sys.stdin.readline().rstrip())
    
counting = 0
    
for _ in range (M) :
    if sys.stdin.readline().rstrip() in seta :
        counting += 1
        
print (counting)