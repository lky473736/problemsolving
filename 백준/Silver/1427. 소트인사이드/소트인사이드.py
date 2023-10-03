N = input()
slist = []

for i in N :
    slist.append (int(i))
    
slist.sort()
slist.reverse()

for j in slist :
    print(j, end="")