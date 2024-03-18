suma = 0

for i in range (5) :
    score = int(input())
    if score < 40 : 
        suma += 40
    
    else :
        suma += score
    
print(suma//5)