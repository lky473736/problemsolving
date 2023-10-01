# 입력이 얼마나 들어올 지 알 수 없는 상황 : EOF -> try, except 사용

while True :
    try : 
        a, b = map(int, input().split())
        print (a + b)
        
    except :
        break
