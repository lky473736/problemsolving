N = int(input())
slist = []

for i in range (N) :
    slist.append(' ' * (N - i - 1) + '*' * (2*i + 1))
    
slist.reverse()

for j in slist : 
    print (j)