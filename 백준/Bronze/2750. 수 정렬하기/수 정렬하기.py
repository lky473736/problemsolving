N = int(input())
slist = []

for i in range (N) :
    compo = int(input())
    slist.append (compo)
    
slist.sort()

for j in slist :
    print (j)