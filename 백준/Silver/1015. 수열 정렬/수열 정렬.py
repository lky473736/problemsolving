# https://nerogarret.tistory.com/31
# https://lighter.tistory.com/18

N = int(input())

A = list(map(int, input().split()))

finder = []

for i in sorted(A) :
    finder.append (i)

slist = []
klist = []

counting = 0 

for j in A :
    if j in finder :
        slist.append(finder.index(j))
        klist.append(finder.index(j))
        
        if slist[-1] in slist[0 : counting] : 
            slist[-1] += klist[0 : counting].count(slist[-1])
        
        counting += 1
        
for p in slist :
    print (p, end = ' ')