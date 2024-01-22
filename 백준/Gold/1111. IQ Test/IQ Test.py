import sys

N = int(sys.stdin.readline())

if N == 1 : 
    print ("A")
    exit()
    
list_pattern = list(map(int, sys.stdin.readline().split()))

if N == 2 :
    if list_pattern[0] == list_pattern[1] :
        print (list_pattern[1])
        
    else :
        print ("A")
    
    exit()
    
r = list_pattern[0]
p = list_pattern[1]
q = list_pattern[2]

set_pattern = set(list_pattern.copy())

if len(set_pattern) == 1 :
    print (list(set_pattern)[0])
    exit()

if r-p == 0 :
    print ("B")
    exit()
    
a = (p-q) / (r-p)
b = p - r * a

for i in range (1, N) :
    if list_pattern[i-1] * a + b != list_pattern[i] : 
        print ("B")
        exit()

if a != int(a) or b != int(b) :
    print ("B")
    
else :
    print (int(list_pattern[-1] * a + b))
    