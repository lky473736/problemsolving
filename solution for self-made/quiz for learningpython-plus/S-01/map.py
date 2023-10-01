def smap(i, j) :
    slist = []
    
    for k in j : 
        slist.append(i(k))
        
    return slist

def samplefunc(k) :
    return k ** 2

alist = [1, 2, 3]

print (list(smap(samplefunc, alist)))