# AAAA, BB
# https://www.acmicpc.net/board/view/127333

xdot = input()
xdotlist = list(xdot)

if xdotlist.count('X') % 2 != 0 :
    print (-1)
    exit()
    
else : 
    finder = xdotlist
    startingpoint = 0
    
    for i in range (len(finder)) :
        if xdotlist[i] == '.' :
            if xdotlist[startingpoint : i].count('X') % 2 == 0 : 
                startingpoint = i
                pass
            
            else :
                print (-1)
                exit()
    
for i in xdotlist :
    if 'XXXX' in xdot : 
        xdot = xdot.replace ('XXXX', 'AAAA')
        
    if 'XX' in xdot :
        xdot = xdot.replace ('XX', 'BB')
        
print (xdot)