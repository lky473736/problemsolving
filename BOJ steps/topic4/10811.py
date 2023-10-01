# basket again...

N, M = map(int, input().split())
basket = list(range(1, N + 1))

for _ in range (M) : # 변수 지정 말고 그냥 반복 : _
    i, j = map(int, input().split())
    
    '''if (j - i + 1) % 2 == 0 :
        for _ in range (j - i + 1) :
            basket[i - 1], basket[j - 1] == basket[j - 1], basket[i - 1]
            
    elif (j - i + 1) % 2 != 0 :
        for _ in range (j - i + 1) :'''
        
    # 일부분만 역순 : 슬라이싱 사용
    
    basket[i - 1 : j] = reversed(basket[i - 1 : j])
    
for component in basket :
    print (component, end = ' ')
