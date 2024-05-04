import sys

E, S, M = map(int, sys.stdin.readline().split())

slist = [0, 0, 0]
year = 0

while True : 
    if slist == [E, S, M] :
        break
    
    year += 1
    slist = [slist[0]+1, slist[1]+1, slist[2]+1]
    
    if slist[0] > 15 : 
        slist[0] = 1
    
    if slist[1] > 28 : 
        slist[1] = 1 
        
    if slist[2] > 19 :
        slist[2] = 1
        
print (year)