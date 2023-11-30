dad = list(input().split())
    
mom = list(input().split())
    
union = dad + mom
union = sorted(union)

slist = []

for i in union :
    for j in union : 
        if (i, j) not in slist : 
            print (i, j)
            slist.append ((i, j))