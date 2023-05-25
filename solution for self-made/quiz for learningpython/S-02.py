import turtle

numangle = int(turtle.textinput("", "number of angle?"))

if numangle > 0 :
        len = float(turtle.textinput("", "len?"))
        
        turnangle = 360 - ((180 / numangle) * ((numangle - 2) * numangle))
        
        for i in range (numangle) :
                turtle.forward (len)
                turtle.left (turnangle)
        
elif numangle == 0 :
        rad = float(turtle.textinput("", "rad?"))
        
        turtle.circle (rad)
        
        
turtle.getscreen()._root.destroy()
print ("Exit...")
