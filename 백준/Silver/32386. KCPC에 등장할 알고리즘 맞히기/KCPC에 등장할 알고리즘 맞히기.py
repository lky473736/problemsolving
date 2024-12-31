import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dd = defaultdict(int)

for _ in range(n) :
    line = list(map(str, sys.stdin.readline().split()))
    for tag in line[2:] :
        dd[tag] += 1

sorted_dd = sorted(dd.items(), key=lambda x: -x[1])

try : 
    if sorted_dd[0][1] == sorted_dd[1][1] : 
        print (-1)
        
    else :
        print (sorted_dd[0][0])
    
except : 
    print (sorted_dd[0][0])