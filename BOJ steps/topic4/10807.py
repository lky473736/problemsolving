N = int(input())

# 공백을 기준으로 한 다양한 수를 리스트화 : list(map(int~~~))
L = list(map(int, input().split()))

v = int(input())

print (L.count(v))
