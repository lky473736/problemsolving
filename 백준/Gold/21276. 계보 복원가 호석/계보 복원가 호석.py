import sys
from collections import defaultdict, deque

ancestor = list()
parents = defaultdict (list)
childrens = defaultdict (list)
indegree = defaultdict (int)

rst = defaultdict(list)

def topology (root) :
    # https://coooco.tistory.com/70
    q = deque()
    q.append(root)

    while q :
        current = q.popleft() # 가장 앞에 있는거 뺌
        
        for children in childrens[current] : # 현재 current(부모)의 아이
            indegree[children] -= 1 # 조상의 수를 하나씩 뺌
            
            if indegree[children] == 0 : # 만약 0이면 (그니깐 조상이 없으면) 그게 부모 
                rst[current].append(children) # 부모 : 아이
                q.append(children) # children을 다시 넣음
 
N = int(sys.stdin.readline())
names = list(sys.stdin.readline().rstrip().split())

M = int(sys.stdin.readline())
for i in range (M) :
    X, Y = sys.stdin.readline().rstrip().split()
    
    parents[X].append (Y)  # parents 안에는 아이 : 부모 이런 형식으로 저장됨
    childrens[Y].append (X) # childrens 안에는 부모 : 아이 이런 형식으로 저장됨
    
    indegree[X] += 1 # indegree는 아이가 key (아이의 조상의 수를 의미함)
    
cnt_ancestor = 0
for name in names : # 조상 찾기
    if parents[name] :  # 부모가 있으면
        continue
    
    ancestor.append (name) # 부모가 없으면 조상임
    cnt_ancestor += 1

names = sorted(names)

print (cnt_ancestor)
for compo in sorted(ancestor) : 
    print (compo, end = ' ')
    
print ()

for root in ancestor : 
    topology(root)
    
for name in names : 
    print (f'{name} ', end = '')
    
    if rst[name] : 
        print (len(rst[name]), end = ' ')
        
        for compo in sorted(rst[name]) : 
            print (compo, end=' ')
        
    else : 
        print (0, end=' ')
    
    print ()
    