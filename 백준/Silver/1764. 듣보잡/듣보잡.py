import sys

N, M = map(int, sys.stdin.readline().split())

nlist = []
dbj = []
counting = 0

for _ in range (N) : 
    nlist.append (sys.stdin.readline().rstrip())
    
nlist.sort()
    
for _ in range (M) :
    compo = sys.stdin.readline().rstrip()
    
    start = 0
    end = N - 1

    while start < end :
        mid = (start + end) // 2

        if compo > nlist[mid] :
            start = mid + 1

        else :
            end = mid
            
    if compo == nlist[start] :
        counting += 1
        dbj.append (compo)
        
print (counting)

for i in sorted(dbj) : 
    print (i)