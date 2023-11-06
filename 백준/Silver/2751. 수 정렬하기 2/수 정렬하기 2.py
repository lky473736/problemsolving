N = int(input())

nlist = []

for i in range (N) :
    compo = int(input())
    nlist.append(compo)
    
nlist.sort()
nset = set(nlist)

for j in nset :
    print (j)