N = int(input())
finder = 1

if N == 1 :
    print (0)
    exit()

while finder <= N : 
    finder = str(finder)
    finder_list = list(finder)
    
    finder_list.sort(reverse = True)
    
    suma = 0
    
    for i in range (len(finder)) :
        suma += int(finder_list[i])
        
    finder = int(finder)
    
    if N == suma + finder : 
        print (finder)
        exit()
    
    else :
        finder += 1
        
print (0)