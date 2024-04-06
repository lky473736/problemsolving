import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque()
lst = list()

for i in range (N) :
    queue.append(i+1)

# 제거 : get, 추가 : put

while N > 0 : 
    # print (queue[2])
    
    ind = 0
    
    for i in range (K) :
        if ind == K : 
            ind = 0
            
        ind += 1
    
    for i in range (ind-1) :
        t = queue.popleft()
        queue.append(t)
    
    l = queue.popleft()
    lst.append (l)
    
    N -= 1
    
# print (lst)

# while N > 0 :
#     if temp 
    
#     N -= 1
    
print ("<", end="")
for compo in lst[:-1] :
    print (str(compo) + ", ", end="")
print (str(lst[-1]) + ">")