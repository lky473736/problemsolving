# import sys
# import heapq

# N, M, K = map(int, sys.stdin.readline().split())
# factory = list(map(int, sys.stdin.readline().split()))
# edge = [[] for _ in range (N)]
# visited = [-1 for i in range (N)]

# min_heap = heapq.heapq()
# for compo in factory : 
#     min_heap.heappush((0, compo-1)) 
#     # 가중치 0 -> 전기 생산
    
# for i in range (M) :
#     node_1, node_2, weight = map(int, sys.stdin.readline().split())
    
#     edge[node_1].append ((weight, node_2-1))
#     edge[node_2].append ((weight, node_1-1))
    
# while min_heap : 
#     weight, number = heapq.heappop(min_heap)
    
#     if visited[number] == -1 :
#         visited[number] = weight
        
#         for next in edge[number] :
#             min_heap.heappush((next[0], next[1]))
            
# print (sum(visited))

import sys
import heapq
import math

N, M, K = map(int, sys.stdin.readline().split()) 
factory = list(map(int, sys.stdin.readline().split()))

edges = [[] for _ in range(N)]
visited = [-1 for _ in range (N)]

for _ in range (M) :
    node_1, node_2, weight = map(int, sys.stdin.readline().split())
    
    edges[node_1-1].append((weight, node_2-1))
    edges[node_2-1].append((weight, node_1-1))

min_heap = []
dist = [math.inf] * N

for compo in factory : 
    heapq.heappush(min_heap, (0, compo - 1)) # 발전소만 heap에 넣기

while min_heap : # 최소힙이 없어질때까지 (발전소)
    current_weight, node = heapq.heappop(min_heap) 

    if visited[node] == -1 :  # 전기가 연결이 안되어있으면
        visited[node] = current_weight 
        
        for cursor in edges[node] : # 연결도시
            heapq.heappush(min_heap, (cursor[0], cursor[1]))

print (sum(visited))