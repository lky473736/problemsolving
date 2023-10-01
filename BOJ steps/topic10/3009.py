# https://www.acmicpc.net/board/view/98620

xlist = [0, 0, 0, '_']
ylist = [0, 0, 0, '_']

for i in range (3) :
    A, B = map(int, input().split())
    xlist[i], ylist[i] = A, B
    
for i in xlist : 
    if xlist.count(i) != 1 :
        pass
    
    elif xlist.count(i) == 1 :
        xlist[3] = i
        
for i in ylist : 
    if ylist.count(i) != 1 :
        pass
    
    elif ylist.count(i) == 1 :
        ylist[3] = i
        
print (xlist[3], ylist[3])
