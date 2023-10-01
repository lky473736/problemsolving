slist = []

while True : 
    A, B = map (int, input().split())
    
    if A == B == 0 : 
        break
    
    slist.append (A + B)
    
for i in slist : 
    print (i)
