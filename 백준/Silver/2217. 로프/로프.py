import sys

N = int(sys.stdin.readline())

rope = []

for _ in range (N) : 
    r = int(sys.stdin.readline())
    rope.append (r)
    
if N == 1 :
    print (r)
    exit()
    
maximum = 0 

rope.sort(reverse = True)

for i in range (N) : 
    compare = rope[i] * (i + 1)
    if maximum < compare : 
        maximum = compare
        
print (maximum)