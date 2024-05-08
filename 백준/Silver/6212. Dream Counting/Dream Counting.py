import sys

M, N = map(int, sys.stdin.readline().split())
ndict = dict()

for i in range (0, 10) :
    ndict[str(i)] = 0
    
for num in range (M, N + 1) :
    string = str(num)
    
    for char in string : 
        ndict[char] += 1
        
print (*ndict.values())