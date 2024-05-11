import sys

n = 0
numbers = []
token = 0

while True : 
    try :
        line = list(map(str, sys.stdin.readline().rstrip().split()))
        
    except : 
        break
    
    if token == 0 :
        n = int(line[0])
            
        for word in line[1:] : 
            numbers.append (int(word[::-1]))
            n -= 1 
            
        token = 1
                
    else :
        for word in line : 
            numbers.append (int(word[::-1]))
            n -= 1
            
    if n == 0 :
        break
        
for compo in sorted(numbers) :
    print (compo)