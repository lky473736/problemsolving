import sys

def euclidean (X, Y) :
    a = Y 
    b = X % Y 
    p = 0
    
    if b == 0 :
        return a
    
    while True :
        p = a % b
        
        if p == 0 :
            break
        
        a = b
        b = p
        
    return b

K, N = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

i = 0
prev, gcd, lcm = 0, 0, 0

while i < N :
    if i == 0 :
        prev = arr[i];
        
    else :
        gcd = euclidean(prev, arr[i])
        lcm = (prev * arr[i]) // gcd
        prev = lcm
        # print (prev, gcd, lcm)
    
    i += 1
    
print (lcm - K)
    
    

# password = 0
# token = 0

# while True : 
#     if token == 1 :
#         break
    
#     for_token = 0
    
#     for compo in arr : 
#         if compo - password % compo != K : 
#             for_token = 1 
#             password += 1 
#             break
        
#     if for_token == 1 : 
#         continue
        
#     token = 1
    
# print (password)