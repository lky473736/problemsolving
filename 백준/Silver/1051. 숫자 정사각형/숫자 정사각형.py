N, M = map(int, input().split())

slist = []
finder = []

for _ in range (N) : 
    num = list(input())
    slist.append([int(compo) for compo in num])
    # slist.append (list(map(int, num)))

for i in range (N) : 
    for p in range (M) : 
        for q in range (M) :
            length = abs(q - p) + 1

            if length + i <= N and length + q <= M :
                if slist[length + i - 1][q] == slist[length + i - 1][p] == slist[i][p] == slist[i][q] :
                        finder.append (length**2)
                        
if finder == [] :
    print (1)

else :
    print (max(finder))