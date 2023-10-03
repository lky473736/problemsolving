aaah_list = []

for i in range (2) :
    ah = input()
    aaah_list.append (ah)
    
if aaah_list[0].count('a') >= aaah_list[1].count('a') :
    print ("go")
    
else :
    print ("no")