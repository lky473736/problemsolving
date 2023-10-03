'''N = int(input())

if N == 1 :
    print ('*')

else : 
    middle = N
    
    for i in range (0, N) :
        print ('*' * (i + 1) + ' ' * (2*N -2*i - 2) + '*' * (i + 1))
    
    for i in range (0, N - 1) : 
        print ('*' * (N - i - 1) + ' ' * (2*i + 2) + '*' * (N - i - 1))'''
        
n = int(input())

# 상단 삼각형 출력
for i in range(1, n + 1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)

# 하단 삼각형 출력
for i in range(n - 1, 0, -1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)