# gomgomtikon

N = int(input())
slist = []
i = 1

for i in range (N) :
    compo = slist.append(input())

position_enter = []

for j in range (len(slist)) :
    if slist[j] == "ENTER" : 
        position_enter.append (j)

suma = 0

if len(position_enter) >= 2 :
    for k in range (len(position_enter)) :
        if k == len(position_enter) - 1 :
            suma += len(set(slist[position_enter[k] :]))
            break
            
        suma += len(set(slist[position_enter[k] : position_enter[k + 1]]))
        
    print (suma - len(position_enter))
        
elif len(position_enter) == 1 :
    print (len(set(slist)) - 1)