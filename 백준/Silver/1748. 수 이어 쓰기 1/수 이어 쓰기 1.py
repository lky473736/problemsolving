N = int(input())
pointer = 9 # 1의 자리 수는 이미 저장

if N <= 9 :  # 1의 자리
    print (N * 1)

else :
    length = len(str(N))
    
    if length > 2 : # 3의 자리 이상
        for i in range (2, length) : 
            pointer += i * (int(str(9) + '9' * (i - 1)) - 10**(i-1) + 1)
            
        # 주어진 N의 일의 자리 수부터 계산하여 해당 위치의 숫자까지를 합산
        result = pointer + length * (N - (10 ** (length - 1)) + 1)
        print(result)

        
    else : # 2의 자리
        pointer += (N - 9) * 2 
        
        print (pointer)