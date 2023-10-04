N = int(input())

baseball = list(map(int, input().split()))

original = sorted(baseball)

bbada = 0

for i in range (N) : 
    if baseball[i] == original[i] :
        pass
    
    else :
        bbada += 1
        
print (bbada)