def find_first_look_up_cows(n, heights):
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and heights[stack[-1]] < heights[i]:
            result[stack.pop()] = i + 1
        stack.append(i)
    
    return result

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
heights = [int(data[i]) for i in range(1, N+1)]

# 결과 계산
result = find_first_look_up_cows(N, heights)

# 결과 출력
for r in result:
    print(r)
