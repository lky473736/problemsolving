A, I = map(int, input().split())

x = 0
k = 0

while True : 
    K = int(x / A) + 1 
    
    if K == I :
        break
    
    x += 1 
    
print (x + 1)