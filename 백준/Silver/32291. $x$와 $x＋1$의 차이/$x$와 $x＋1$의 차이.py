import sys
import math

# for x in range (1, 21) : 
    # # x = int(sys.stdin.readline())
    # y = x + 1
    
    # # nlist = []
    # # for i in range (1, y) :
    # #     if x // i != y // i :
    # #         nlist.append (i)
            
    # # print (x, *nlist)

x = int(sys.stdin.readline())
y = x + 1

slist = []
cnt = 0

for i in range(1, int(math.sqrt(y)) + 1):
    if y % i == 0 :
        slist.append(i) 
        cnt += 1
        
        if i != y // i :          
            slist.append(y // i)
            cnt += 1
            
# print (slist)
if cnt == 2 :
    # slist.pop()
    print (slist[0])
    
else : 
    print (*sorted(slist)[:-1])