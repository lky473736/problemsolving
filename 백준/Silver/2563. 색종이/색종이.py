N = int(input())
total_black_area = 0

# 도화지 크기
canvas_size = 100

# 흰 도화지 초기화
white_canvas = [[0] * canvas_size for _ in range(canvas_size)]

for _ in range(N):
    x, y = map(int, input().split())
    
    # 색종이의 왼쪽 위 모서리 좌표를 계산
    left = x
    top = canvas_size - y - 10
    
    # 색종이 영역을 1로 채움
    for i in range(top, top + 10):
        for j in range(left, left + 10):
            white_canvas[i][j] = 1

# 흰 도화지에서 검은 영역의 넓이를 계산
for i in range(canvas_size):
    for j in range(canvas_size):
        if white_canvas[i][j] == 1:
            total_black_area += 1

print(total_black_area)