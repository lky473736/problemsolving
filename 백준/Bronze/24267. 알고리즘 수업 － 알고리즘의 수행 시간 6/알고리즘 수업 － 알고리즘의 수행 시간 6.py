n = int(input())
suma = 1
finder = []

if n == 1 or n == 2 :
    print (0)
    print (3)
    exit()

if n == 3 : 
    print (1)
    print (3)
    exit()
    
for i in range (n - 3) : 
    suma += 2 + i
    finder.append (suma)
    
    
print (sum(finder) + 1)
print (3)