'''import sys

N = int(sys.stdin.readline())

lst = []
num = 0
key = 0
max = 0
counting = 0

while True : 
    num += 1
    k1 = num
    k2 = N - num
    seta = set([k1])
    counting = 1
    
    while True :
        if k2 in seta :
            break
            
        elif k2 == 0 :
            key = 1
            break
        
        k1 += 1
        k2 = k2 - k1
        
        seta.add(k1)
        counting += 1
        
    lst.append(len(list(seta)))
    
    if max < counting : 
        max = counting
    
    if key == 1 :
        break
    
print (max(lst))
print (max)'''

# https://mgyo.tistory.com/780 참고

import sys

N = int(sys.stdin.readline())
sum = 0
rst = 0

for i in range (1, N + 1) :
    sum += i
    rst = i
    
    if sum > N : 
        rst = rst - 1
        break

print (rst)