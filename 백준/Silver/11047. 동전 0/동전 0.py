import sys

unit = list()

N, K = map(int, sys.stdin.readline().split())

for _ in range (N) : 
    compo = int(sys.stdin.readline())
    unit.append(compo)
    
unit.sort(reverse = True)

coin = 0
i = 0
    
while K != 0 and i < N :
    if unit[i] <= K :
        coin += (K // unit[i])
        K -= (K // unit[i]) * unit[i]
            
    else :
        pass
    
    i += 1
        
print (coin)