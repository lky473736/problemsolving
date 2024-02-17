import sys
import itertools

X = list(sys.stdin.readline().rstrip())
permu = list(itertools.permutations(X, len(X)))
lst = []

for i in permu :
    if int(''.join(X)) < int(''.join(i)) : 
        lst.append (int(''.join(i)))

if lst == [] :
    print (0)
    exit()
    
lst.sort()
print (lst[0])