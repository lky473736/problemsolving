anglelist = []

for i in range (3) :
    angle = int(input())
    anglelist.append(angle)

if sum(anglelist) == 180 :
    if anglelist.count(60) == 3 :
        print ("Equilateral")
        exit()
    
    elif anglelist[0] == anglelist[1] or anglelist[1] == anglelist[2] or anglelist[0] == anglelist[2] :
        print ("Isosceles")
        exit()
            
    else :
        print ("Scalene")
        exit()
            
else : 
    print ("Error")