import sys
from itertools import permutations

inp = -1

while True :
    inp = list(map(int, sys.stdin.readline().split()))
    
    if inp == [0] :
        break
    
    k = inp[0]
    tc = inp[1:]
    
    for i in permutations(tc, 6) :
        if sorted(list(i)) == list(i) :
            rst = ' '.join(str(s) for s in i)
            # print (i)
            print (rst)
    
    print ()