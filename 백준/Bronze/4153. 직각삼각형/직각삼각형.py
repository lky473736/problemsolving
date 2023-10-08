while True : 
    length = list(map(int, input().split()))
    
    if length.count(0) == 3 :
        exit()

    length.sort()

    if length[2] ** 2 == length[0] ** 2 + length[1] ** 2 :
        print ("right")
    
    else : 
        print ("wrong")