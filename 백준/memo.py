# hot italy

N, M = map(int, input().split())

donot = [[] for i in range (N)]
finder = []

for i in range (M) :
    com1, com2 = map(int, input().split())
    donot[com1 - 1].append (com2)
    
for i in range (N) :
    for j in range (N) : 
        if j + 1 not in donot[i] and i + 1 not in donot[j] and j + 1 != i + 1 : 
            for k in range (N) :
                if j + 1 not in donot[i] and i + 1 not in donot[j] and k + 1 not in donot[i] and k + 1 not in donot[j] and j + 1 not in donot[k] and i + 1 not in donot[k] and k + 1 != j + 1  :
                    if set([i + 1, j + 1, k + 1]) not in finder and len(set([i + 1, j + 1, k + 1])) == 3 :
                        finder.append (list([i + 1, j + 1, k + 1]))


list_of_sets = finder
unique_sets = [tuple(sorted(set(x))) for x in list_of_sets]
result = list(set(unique_sets))

print (len(result))
