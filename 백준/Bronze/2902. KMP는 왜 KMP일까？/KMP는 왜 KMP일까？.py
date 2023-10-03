name = input()

upperlist = [name[0]]

for i in range (len(name)) :
    if name[i] == '-' :
        upperlist.append (name[i+1])
        
for j in upperlist :
    print (j, end = '')