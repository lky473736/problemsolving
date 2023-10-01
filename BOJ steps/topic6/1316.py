N = int(input())

slist = []
total_count = 0

for i in range (N) :
    string = input()
    slist.append (string)
    
for k in slist :
    tlist = []
    
    for j in range (len(k)) :
        if j == 0 :
            tlist.append (1)
        
        else :
            if k[j] != k[j - 1] :
                if k[j] not in k[ : j] :
                    tlist.append (1)
                
                else :
                    tlist.append (0)
            
            elif k[j] == k[j - 1] :
                tlist.append (1)
                
    if 0 not in tlist :
        total_count = total_count + 1

print (total_count)
