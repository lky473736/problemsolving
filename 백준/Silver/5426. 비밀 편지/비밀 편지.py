import sys

T = int(input())

for i in range (T) :
    message = sys.stdin.readline().rstrip()
    length = int(pow(len(message), 0.5))
    
    slist = []
    
    for p in range (length) : 
       slist.append (message[p*length:p*length + length][::-1])
       
    for x in range (length) : 
        for y in range (length) : 
            print (slist[y][x], end = "")
            
    print ()