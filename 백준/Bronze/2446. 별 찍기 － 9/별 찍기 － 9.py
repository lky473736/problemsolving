N = int(input())
slist = []

for i in range (N) :
    slist.append(' ' * (N - i - 1) + '*' * (2*i + 1))
    
klist = list(reversed(slist))

klist.remove(klist[-1])

for k in klist :
    print (k)

for j in slist : 
    print (j)