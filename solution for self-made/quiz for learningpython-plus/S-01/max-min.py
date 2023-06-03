def smax (k) :
    k.sort()
    return k[-1]

def smin (k) :
    k.sort()
    return k[0]

slist = [-1, -2, -3, -4, -5, 100]

print (smax(slist))
print (smin(slist))