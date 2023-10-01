N, K = map(int, input().split())
slist = []

for i in range (N) :
    if N % (i + 1) == 0 :
        slist.append (i + 1)

if len(slist) < K :
    print (0)
    exit()
    
print (slist[K - 1])
