X = int(input())
N = int(input())

slist = []

for i in range(N) :
    a, b = map (int, input().split())
    slist.append (a * b)

if sum (slist) == X :
    print ('Yes')
    
else : 
    print ('No')
