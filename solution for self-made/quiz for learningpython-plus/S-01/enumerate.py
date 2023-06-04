# 1 : component가 list인 enumerate
'''def senumerate(k) :
    slist = []
    num = 0
    
    for i in range (len(k)):
        plist = []
        plist.append (i)
        slist.append (plist)
        
    for j in k :
        slist[num].append (j)
        num += 1
    
    return slist
        
alist = [1, 2, 3, 4, 5]
print (list(senumerate(alist)))'''

# 2 : component가 tuple인 원래 enumerate
def senumerate(k) :
    slist = []
    
    for i in range(len(k)) :
        slist.append((i, k[i]))
        
    return slist

alist = [1, 2, 3, 4, 5]
print(list(senumerate(alist)))
