import sys

n = int(sys.stdin.readline())
slist = list(map(int, sys.stdin.readline().split()))

slist.sort()

semi = 10000000
for i in range (n) :
    # print (slist[i], slist[-1-i])
    
    if slist[i] + slist[-1-i] < semi : 
        semi = slist[i] + slist[-1-i]
        
    else :
        pass
    
print (semi)