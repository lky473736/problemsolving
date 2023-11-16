''' # 아래것이 도대체 왜 안되는지 모르겠음

import sys 

input = sys.stdin.readline().rstrip()
T = int(input)

for i in range (T) :
    a1 = tuple(map(int, sys.stdin.readline().rstrip().split()))
    a2 = tuple(map(int, sys.stdin.readline().rstrip().split()))
    a3 = tuple(map(int, sys.stdin.readline().rstrip().split()))
    a4 = tuple(map(int, sys.stdin.readline().rstrip().split()))
    
    finder = [a1, a2, a3, a4]
    
    print (finder)
    
    # 정렬 방법 출처 : https://shortcuts.tistory.com/39
    # x좌표 오름차순 정렬 후 y좌표 오름차순 정렬
    finder.sort()
    
    # 첫 번째 방법 : 두 대각선의 길이 동일 및 두 대각선의 기울기의 곱이 -1
    
    diagonal1 = ((finder[1][0] - finder[2][0])**2 + (finder[1][1] - finder[2][1])**2) ** 0.5 # 대각선 1
    diagonal2 = ((finder[3][0] - finder[0][0])**2 + (finder[3][1] - finder[0][1])**2) ** 0.5 # 대각선 2
    
    if finder[3][0] - finder[0][0] == 0 or finder[2][0] - finder[1][0] == 0 :
        slobe1, slobe2 = 0, 0 
        
    else : # 기울기
        slobe1 = (finder[3][1] - finder[0][1]) / (finder[3][0] - finder[0][0])
        slobe2 = (finder[2][1] - finder[1][1]) / (finder[2][0] - finder[1][0])
                
    if diagonal1 == diagonal2 : # 대각선 크기가 서로 같으면
        if slobe1 * slobe2 == -1 : # 기울기가 서로 수직이면
            print (1)
            
        else :
            print (0)
            
    else :
        print (0)
        
    # 두 번째 방법 : 두 대각선의 길이 동일 및 피타고라스 성립
        
    diagonal1_squared = (finder[1][0] - finder[2][0]) ** 2 + (finder[1][1] - finder[2][1]) ** 2
    diagonal2_squared = (finder[3][0] - finder[0][0]) ** 2 + (finder[3][1] - finder[0][1]) ** 2

    if diagonal1_squared == diagonal2_squared and diagonal1_squared == (finder[2][0] - finder[0][0])**2 + (finder[2][1] - finder[0][1])**2 + (finder[0][0] - finder[1][0])**2 + (finder[0][1] - finder[1][1])**2 : 
        print(1)
        
    else:
        print(0)'''
        
import sys

def distance_squared(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def is_square(a, b, c, d):
    distances = [distance_squared(a, b), distance_squared(a, c), distance_squared(a, d),
                 distance_squared(b, c), distance_squared(b, d), distance_squared(c, d)]
    distances.sort()
    return distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]

T = int(input().rstrip())

for _ in range(T):
    points = []
    for _ in range(4):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        points.append((x, y))

    if is_square(points[0], points[1], points[2], points[3]):
        print(1)
    else:
        print(0)