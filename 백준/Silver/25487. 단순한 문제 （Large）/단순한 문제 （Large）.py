import sys

T = int(sys.stdin.readline())

for _ in range (T) :
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a <= b and a <= c : 
        print (a)
        
    elif b <= a and b <= c :
        print (b)
        
    elif c <= a and c <= b :
        print (c)

