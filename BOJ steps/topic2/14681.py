component_x = int(input())
component_y = int(input())

if component_x > 0 :
    if component_y > 0 :
        print ("1")
        
    elif component_y < 0 :
        print ("4")

elif component_x < 0 :
    if component_y > 0 :
        print ("2")  
        
    elif component_y < 0 :
        print ("3")
