import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

time = list()
timeset = set()
timedict = dict()

for _ in range (N) :
    ki, ti = map(int, sys.stdin.readline().split())
    time.append (ki)
    
    if ki not in timeset : 
        timeset.add(ki)
        timedict[ki] = [ti]
        
    else :
        timedict[ki].append (ti)

time.sort()
minute = 0
i = 0

for number in p :
    lst = sorted(timedict[i+1])
    j = 0
    
    while j != number :
        minute += lst[j]
        
        if j != number - 1 : 
            minute += lst[j+1] - lst[j]
        
        j += 1
        
    i += 1
    
    if i != len(p) : 
        minute += 60

print (minute)