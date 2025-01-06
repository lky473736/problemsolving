while True : 
    stri = input()
    if stri == '#' :
       break
    cnt = 0
    for i in range (len(stri)) : 
        if stri[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] : 
            cnt += 1
            
    print (cnt)