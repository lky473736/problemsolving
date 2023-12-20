'''position = []
intersection = []
size = 0'''

''' 수식적인 풀이
for _ in range (4) : 
    x1, y1, x2, y2 = map(int, input().split())
    
    if position != [] :
        for i in position : 
            xset = set.intersection (set([j for j in range (x1, x2+1)]), set(j for j in range (i[0], i[2]+1)))
            yset = set.intersection (set([j for j in range (y1, y2+1)]), set(j for j in range (i[1], i[3]+1)))
            
            if len(xset) != 0 and len(yset) != 0 :
                intersection.append ([xset, yset])
    
    position.append([x1, y1, x2, y2])
    size += (x2 - x1) * (y2 - y1)
    
print (intersection)'''

suma = 0

# 2차원 배열을 만들어서 풀이
cartesian = [[0 for i in range (101)] for j in range (101)]

for _ in range (4) : 
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range (y2 - y1) :
        for j in range (x2 - x1) :
            cartesian[y1+i][x1+j] = 1
            
cartesian = cartesian[::-1]

for row in cartesian : 
    suma += row.count(1)
    
print (suma)