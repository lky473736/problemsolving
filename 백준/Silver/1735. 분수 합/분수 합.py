P, Q = map(int, input().split())
A, B = map(int, input().split())

# P / Q, A / B 

Y = Q * B # 분모
X = Q * A + P * B # 분자

''' 기본적인 알고리즘 (linear하기 때문에 시간 초과)
for i in range (1, X + 1) :
    if X % i == 0 and Y % i == 0 :
        X = X // i 
        Y = Y // i
        
if X // Y == 1 :
    print (1, 1)
    exit()

if X % Y == 0 :
    print (X // Y, Y // (X // Y))
    
elif Y % X == 0 :
    print (Y // X, X // (Y // X))

else :    
    print (X, Y)'''
    
# 유클리드 호제법을 사용하여 최대공약수 구하고 사용

def euclidean (X, Y) :
    a = Y 
    b = X % Y 
    p = 0
    
    if b == 0 :
        return a
    
    while True :
        p = a % b
        
        if p == 0 :
            break
        
        a = b
        b = p
        
    return b
    
gcd = euclidean(max(X, Y), min(X, Y))

print (X // gcd, Y // gcd)