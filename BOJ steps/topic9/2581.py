M = int(input())
N = int(input())

slist = list(range(M, N + 1))
rst = []

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
        rst.append (i)

if len(rst) > 0:
    print(sum(rst))
    print(rst[0])
else:
    print(-1)
