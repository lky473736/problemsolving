string = input()

if string[0] != ' ' and string[-1] != ' ' :
    print (string.count(' ') + 1)
    
elif string[0] == ' ' and string[-1] != ' ' :
    print (string.count(' '))
    
elif string[0] != ' ' and string[-1] == ' ' :
    print (string.count(' '))
    
else : 
    print (string.count(' ') - 1)
