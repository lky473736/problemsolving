import sys

slist = [1, 2]
ind = 2

while True : 
    if slist[ind-1] + slist[ind-2] <= 4000000 : 
        slist.append (slist[ind-1] + slist[ind-2])
    else : 
        break
    
    ind += 1

print (slist)

rst = 0
for i in slist :
    if i % 2 == 0 : 
        print (i, end = ' ')
        rst += i
        
print ("\n", rst)
