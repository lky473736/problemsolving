while True :
    length = list(map(int, input().split()))
    
    if length == [0, 0, 0] :
        break
    
    else : 
        if sorted(length)[-1] < sorted(length)[0] + sorted(length)[1] :
                if length.count(length[0]) == 3 :
                    print ("Equilateral")
            
                elif length[0] == length[1] or length[1] == length[2] or length[0] == length[2] :
                    print ("Isosceles")
        
                elif length[0] != length[1] and length[1] != length[2] and length[0] != length[2] :
                    print ("Scalene")
                    
        else : 
            print ("Invalid")
            