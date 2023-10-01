T = int(input())
slist = []
 
for i in range (T) :
    A, B = map(int, input().split())
    slist.append (A + B)
    
for j in range (T) : 
    print (f'Case #{j + 1}: ' + str(slist[j]))
