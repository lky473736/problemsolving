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

# 색종이 검정 부분 : 겹치는 부분 
# 겹치는 부분의 가로와 세로의 총합끼리 곱하면 될 것 같다
# 겹치는 부분을 구하기 위해서 set으로 선언 후 intersection 

'''N = int(input())
colorpaperx = []
colorpapery = []

x_len = 0
y_len = 0

for i in range (N) :
    component = list(map(int, input().split()))
    colorpaperx.append (set(range(component[0], component[0] + 11)))
    colorpapery.append (set(range(component[1], component[1] + 11)))

'''for j in range (N) :
    x_intersection = set.intersection(colorpaperx[j], colorpaperx[j+1])
    y_intersection = set.intersection(colorpapery[j], colorpapery[j+1])
    
    if len(x_intersection) > 1 and len(y_intersection) > 1 :
        x_len += len(x_intersection)
        y_len += len(y_intersection)'''
        
'''for j in range (N):
    # 현재 색종이와 다음 색종이 간의 교차 부분 계산
    next_index = (j + 1) % N  # 다음 색종이의 인덱스 계산
    x_intersection = set.intersection(colorpaperx[j], colorpaperx[next_index])
    y_intersection = set.intersection(colorpapery[j], colorpapery[next_index])

    if len(x_intersection) > 1 and len(y_intersection) > 1:
        x_len += len(x_intersection)
        y_len += len(y_intersection)'''

# 겹친 부분 구하기
x_inter = colorpaperx[0]
y_inter = colorpapery[0]
counter = 0
    
for j in range (N) :
    if j == N - 1 :
        x_inter = x_inter.intersection (colorpaperx[-1])
        y_inter = y_inter.intersection (colorpapery[-1])
        break
        
    x_inter = x_inter.intersection (colorpaperx[j + 1])
    y_inter = y_inter.intersection (colorpapery[j + 1])
    
    counter += 1
    
    if x_inter == set() :
        x_inter = colorpaperx[j]
    
    if y_inter == set() :
        y_inter = colorpapery[j]

inter_teratory = (len(list(x_inter)) - 1) * (len(list(y_inter))-1)

# 원래 사각형 넓이 - 겹친 부분

print (N * 100 - inter_teratory * counter)'''
