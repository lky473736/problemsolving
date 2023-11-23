def fact (m) : 
    if m <= 1 :
        return 1
        
    else :
        return m * fact(m - 1)

def combination (n, m) : 
    permu = fact(n) // fact(n-m)
    
    return permu // fact(m)
    
n, m = map(int, input().split())

print (combination(n, m))