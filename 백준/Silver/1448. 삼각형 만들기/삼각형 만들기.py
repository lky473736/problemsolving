import sys 
input = sys.stdin.readline().rstrip()
N = int(input)

slist = []
rst = []

for i in range (N) : 
    input = sys.stdin.readline().rstrip()
    compo = int(input)
    slist.append (compo)
    
slist.sort()

for j in range (2, N) :
    finder = slist
    longth = finder[j]
    
    if longth < finder[j-1] + finder[j-2] :
        rst.append (longth + finder[j-1] + finder[j-2])
            
if rst == [] :
    print (-1)
    
else :
    print(max(rst))