import sys
from collections import Counter 

N = int(input())

numlist = []

suma = 0

for _ in range (N) : 
    num = int(sys.stdin.readline())
    numlist.append(num)
    
    suma += num
    
numlist.sort()

mean = round(suma / N)
mid = numlist[N//2]
cnt = Counter(numlist)
sorted_items = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

max_freq = sorted_items[0][1] 
value = cnt.values()
modes = [k for k, v in sorted_items if v == max_freq]  # 최빈값들을 리스트로 추출

if len(modes) >= 2 : 
    mode = modes[1]

else :
    mode = modes[0]

dt_range = numlist[-1] - numlist[0]

print (mean)
print (mid)
print (mode)
print (dt_range)