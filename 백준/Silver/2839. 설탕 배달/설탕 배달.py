N = int(input())

finder = []

way1 = 5001
way2 = 5001
way3 = 5001

if N == 3 or N == 5 : 
    print (1)
    exit()

if N % 5 == 0 : 
    way1 = N // 5
    
if N % 3 == 0:
    way2 = N // 3

five = N // 5

for i in range (five) :
    if (N - (i + 1) * 5) % 3 == 0 : 
        rest = (N - (i + 1) * 5) // 3
        finder.append (i+1+rest)
        
if finder != [] :
    way3 = min(finder)

if way1 != 5001 or way2 != 5001 or way3 != 5001 :
    print(min(min(way1, way2), way3))
    
else :
    print (-1)