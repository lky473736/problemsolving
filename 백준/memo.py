import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

lst = set()

for i in range (M+1) : 
    for j in itertools.permutations(sequence, N - i) : 
        for k in itertools.permutations(j, 2) :
            print (k)
            if k[0] < k[1] :
                lst.add (k[1]-k[0])
                print (lst)
            
            print ('-' * 10)
                
print (lst)
...
