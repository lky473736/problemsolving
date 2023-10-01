a, b, c = map(int, input().split())
a = int(a)
b = int(b)
c = int(c)

slist = [a, b, c]
numlist = []

slist.sort()

for i in range (6) :
    if slist.count (i + 1) > 0 :
        numlist.append (slist.count (i + 1))
    
    else : 
        numlist.append (0)

if 3 in numlist : 
    print (10000 + (numlist.index(3) + 1) * 1000)
    exit()
    
if 2 in numlist : 
    print (1000 + (numlist.index(2) + 1)  * 100)
    exit()
    
if 1 in numlist : 
    finder_finalnum = []
    
    for i in range (len(numlist)) :
        if numlist[i] == 1 :
            finder_finalnum.append (1)
            
        else :
            finder_finalnum.append (0)
            
    for j in range (len(numlist)) :
        if finder_finalnum[j] == 1 :
            final_num = j + 1
            
    print (final_num * 100)
    exit()
