import itertools

N, M = map(int, input().split())
numlist = [i for i in range (1, N + 1)]
permu = itertools.permutations (numlist, M)

for compo in permu : 
    for i in compo : 
        print (i, end = ' ')
        
    print ()