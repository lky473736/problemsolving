N, X = map(int, input().split())

# 공백을 기준으로 한 다양한 수를 리스트화 : list(map(int~~~))
A = list(map(int, input().split()))

for i in A : 
    if i < X : 
        print (i, end = " ") # 개행문자 없이 
