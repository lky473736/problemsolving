N = int(input())

if N % 2 == 0 :
    print ("I LOVE CBNU")
    
else : 
    print ('*' * N)
    print (' ' * (((N + 1) // 2)- 1) + '*')
    
    for i in range (((N + 1) // 2)- 1) :
        print (' ' * ((((N + 1) // 2) - 1) - i - 1) + '*' + ' ' * (2 * i + 1) + '*' * 1)