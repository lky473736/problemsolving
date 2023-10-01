N = int(input())

# 공백을 기준으로 한 다양한 수를 리스트화 : list(map(int~~~))
A = list(map(int, input().split()))

A.sort()

print (A[0], A[-1])
