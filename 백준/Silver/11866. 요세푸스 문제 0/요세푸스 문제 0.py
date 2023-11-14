N, K = map(int, input().split())

queue = [i for i in range (1, N + 1)]
finder = []

point = 0

for j in range (N) :
    point = (point + K - 1) % len(queue)
    
    finder.append (queue[point])
    queue.pop(point)
    
output = '<' + ', '.join(map(str, finder)) + '>'
print(output)