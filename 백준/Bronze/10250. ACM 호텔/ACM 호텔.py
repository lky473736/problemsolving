# ACM

T = int(input())

for i in range (T) : 
    H, W, N = map(int, input().split())

    room = 1
    point = 0
    
    for i in range (1, W + 1) : # room
        if point == 1 :
            break
        
        floor = 0
        
        for j in range (1, H + 1) : # floor
            floor += 1
            
            if (room - 1) * H + floor == N :
                if room < 10 :
                    print (str(floor) + '0' + str(room))
                    point += 1
                    break
                    
                else :
                    print (str(floor) + str(room))
                    point += 1
                    break
        
        room += 1 