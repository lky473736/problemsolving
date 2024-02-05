'''for i in range (2, 10) : 
    counting = 0
    
    for j in range (10**(i-1), 10**(i)) : 
        if set(list(str(j))) == set(['1']) or set(list(str(j))) == set(['1', '5']) or set(list(str(j))) == set(['5']) :
            if j % 15 == 0 :
                counting += 1
                
    print (i, "자릿수 : ", counting)'''
    
N = int(input())

if N == 1 : 
    print (0)
    
elif N == 2 :
    print (1)
    
elif N == 3 :
    print (1)
    
else :
    N -= 3
    
    lst = [1, 1]
    
    while N != 0 : 
        rst = lst[0]*2 + lst[1]
        
        lst[0] = lst[1]
        lst[1] = rst
        
        N -= 1
        
    print (rst % 1000000007)