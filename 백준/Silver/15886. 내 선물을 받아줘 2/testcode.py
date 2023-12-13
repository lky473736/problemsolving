N = int(input())
direction = list(input())

guapple = [0 for i in range (N)]

lengthlist = []
leng = 0
for j in direction : 
        if j == 'E' :
            leng += 1
            lengthlist.append(leng)
            
        else :
            leng -= 1
            lengthlist.append(leng)
            
maxleng = max(lengthlist)

giftlist = [0 for i in range (N)]

for i in range (N - maxleng) : 
    guapple = [0 for i in range (N)]
    indexing = i
    giftnum = 0
    
    for j in direction : 
        if giftlist[indexing] == 1 :
            giftnum += 1
            break 
        
        if j == 'E' :
            indexing += 1
            guapple[indexing] += 1
            
        else :
            indexing -= 1
            guapple[indexing] += 1
        
    if giftnum == 0 :
        giftlist[guapple.index(max(guapple))] = 1

print (giftlist.count(1))
