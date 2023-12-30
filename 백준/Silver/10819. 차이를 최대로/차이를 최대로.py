import itertools 

N = int(input())
arr = list(map(int, input().split()))

suma = 0

for k in itertools.permutations(arr) : 
    nsuma = 0
    for i in range (1, N) : 
        nsuma += abs(k[i-1] - k[i])
        
    if suma < nsuma :
        suma = nsuma

print (suma)