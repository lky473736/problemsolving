# 등차수열의 합 공식 이용

N = int(input())

'''for i in range (N) :
    ox = input()
    olist = []
    
    for j in range (len(ox)) :
        olist.append ([])
    
    j = 0
    l = 0
    
    while j < len(ox) : 
        if ox[j] == 'O' :
            olist[l].append (ox[j])
            j += 1
        
        else :
            l += 1
    
    olist.remove([])
    
    print (olist)
    
    for k in olist :
        n = len(k)
        score = score + (n * (2 + n - 1)) / 2
        
    print (score)'''

for _ in range(N):
    ox = input()
    score = 0  # 점수를 초기화
    
    consecutive_o = 0  # 연속된 'O'의 개수를 초기화
    
    for char in ox:
        if char == 'O':
            consecutive_o += 1
            score += consecutive_o  # 연속된 'O'의 개수를 더해줌
        else:
            consecutive_o = 0  # 'O'가 아닌 경우 연속된 'O'의 개수를 초기화

    print(score)