X, Y = input().split()

# 문자열 뒤집기
X = X[::-1] # X.reverse()
Y = Y[::-1] # Y.reverse()

X = int(X)
Y = int(Y)

print (int(str((X + Y))[::-1]))