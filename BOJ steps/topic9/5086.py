slist = []

X = -1
Y = -1

while X != 0 and Y != 0 : 
    empty = []
    X, Y = map(int, input().split())
    empty.append (X)
    empty.append (Y)
    
    slist.append (empty)

slist.remove (slist[-1])

for i in slist : 
    if i[1] % i[0] == 0 :
        print ('factor')
        
    elif i[0] % i[1] == 0 :
        print ('multiple')
        
    else : 
        print ('neither')
