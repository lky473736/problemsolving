N = int(input())

finder = []

a = list(input())
lengtha = len(a)
a = set(a)
finder.append (a)
length = [lengtha]
    
for i in range(N-1) :
    counting = 0
    
    b = list(input())
    lengthb = len(b)
    b = set(b)
    
    for j in range(len(finder)) : 
        if finder[j] == b and lengthb == length[j] : 
            counting += 1
            
    if counting == 0 : 
        finder.append (b)
        length.append (lengthb)
        
print (len(finder))
    
    