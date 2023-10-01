H, M = input().split()

H = int(H)
M = int(M)

if M < 45 :
    if H == 0 :
        H = 23
        print (str(H) + ' ' + str(60 + (M - 45)))
        exit()
        
    print (str(H - 1) + ' ' + str(60 + (M - 45)))
    
elif M >= 45 and M < 60 :
    print (str(H) + ' ' + str(M - 45))
