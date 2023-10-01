A, B = input().split() # 현재시각
C = input() # 요리시간

A = int(A)
B = int(B)
C = int(C)

'''
min = B + C

if min > 60 :
    if A + min % 60 > 23 : 
        print (str(abs((A + (min // 60)) % 24)) + ' ' + str(min % 60))
        exit()
        
    print (str(abs(A + (min // 60)) % 24) + ' ' + str(min % 60))
        
elif min == 60 : 
    if A + min % 60 > 23 : 
        print (str(abs((A + (min // 60)) % 24)) + ' ' + str(min % 60))
        exit()
        
    print (str(A + 1) + ' ' + str(0))
    
elif min < 60 : 
    if A + min % 60 > 23 : 
        print (str(abs((A + (min // 60)) % 24)) + ' ' + str(min % 60))
        exit()
        
    print (str(A) + ' ' + str(min))'''
    
all_minutes = B + C

time = A + (all_minutes // 60)

if time >= 24 : 
    print (time % 24, all_minutes % 60)
    
elif time < 24 : 
    print (time, all_minutes % 60)
