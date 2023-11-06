N = int(input())
M = int(input())
S = input()
suma = 0

finder = 'IOI' + 'OI' * (N - 1)

for i in range (M) :
    if S[i : i+len(finder)] == finder :
        suma += 1 
        
print (suma)