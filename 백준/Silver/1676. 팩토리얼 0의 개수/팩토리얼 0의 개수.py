N = int(input())

def fact (N) :
    if N == 1 or N == 0 : 
        return 1
    
    else : 
        return N * fact(N - 1)

finder = list(str(fact(N))[::-1])
suma = 0

for i in finder :
    if i != '0' :
        break
    
    if i == '0' :
        suma += 1
        
print (suma)