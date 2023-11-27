# 참고 : https://seunghyum.github.io/algorithm/Euclidean-algorithm/#

def euclidean (x, y) : 
    a = x
    b = y
    
    remainder = 1
    
    while remainder > 0 : 
        remainder = a % b
        a = b
        b = remainder
        
    if remainder == 0 : 
        return a
        
    else :
        return 1

A, B = map(int, input().split())
print (A * B // euclidean(A, B))