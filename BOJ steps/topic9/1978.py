N = int(input())
slist = list(map(int, input().split()))

count = 0

if 1 in slist : 
    slist.remove (1)

for i in slist : 
    yaksu = 0
    
    for j in range (i) :
        if i % (j + 1) == 0 :
            yaksu += 1
            
        else : 
            pass
    
    if yaksu >= 3 :
        pass
    
    else : 
        count += 1

print (count)
    
