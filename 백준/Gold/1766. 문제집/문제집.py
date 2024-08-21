import sys
from collections import defaultdict
import heapq

# https://velog.io/@plate0113/Python-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-heapq
# 우선순위 큐 이용해서 가장 작은값 먼저꺼내기 (왜냐면 쉬운거부터 풀라고 했으니)
# heapq로 자동정렬

def topology() :
    q = []
    
    for i in range(1, N + 1) :
        if indegree[i] == 0 :
            heapq.heappush(q, i)

    while q :
        current = heapq.heappop(q) # 가장 쉬운 것부터 풀기
        rst.append(current) # 현재를 result에 넣기

        for child in graph[current] :
            indegree[child] -= 1
            
            if indegree[child] == 0 : 
                heapq.heappush(q, child)

N, M = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
indegree = defaultdict(int)

for _ in range(M) :
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1

rst = list()
topology()

print (*rst)