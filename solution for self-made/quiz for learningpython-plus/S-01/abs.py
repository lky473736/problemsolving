def sabs(k) :
    k = str(k)
    if k[0] == '-' :
        return k[1:]
    
    else :
        return k

print (sabs(-292837))