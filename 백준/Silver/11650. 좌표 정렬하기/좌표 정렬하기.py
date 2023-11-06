import sys

N = int(sys.stdin.readline().rstrip())
p = []

for i in range(N):
    compo = list(map(int, input().split()))
    p.append(compo)

p.sort(key=lambda x: (x[0], x[1]))  # x 값으로 오름차순 정렬, x 값이 같은 경우 y 값으로 정렬

for k in p:
    x = k[0]
    y = k[1]
    print(x, y)
