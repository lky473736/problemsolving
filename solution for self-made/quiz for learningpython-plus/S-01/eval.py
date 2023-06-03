def seval (k) :
    match (k[1]) :
        case '+' :
            return int(int(k[0])) + int(int(k[2]))
        
        case '-' :
            return int(k[0]) - int(k[2])
        
        case '*' :
            return int(k[0]) * int(k[2])
        
        case '/' :
            return int(k[0]) / int(k[2])
        
print (seval('2+2'))