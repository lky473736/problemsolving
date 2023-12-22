T = int(input())

for _ in range (T) :
    A = input()
    
    alist = [int(i) for i in str(A)] # 받아들인 A를 한 자리씩 리스트화
    lena = len(alist)
    
    if sorted(alist, reverse = True) == alist : # 이미 내림차순이라면
        print ('BIGGEST')
        
    elif lena == 1 : # 한자리라면
        print (A)

    else : # 이외 상황이면
        for i in range (lena - 1) : # 역순 탐색
            if alist[-1 - i] > alist[-1 -1 -i] : 
                break
        
        head = alist[ : -i-1] # 내림차순이 시작되기 전
        temphead = head
        
        tail = alist[-i-1 : ] # 내림차순이 시작된 부분부터
        temptail = tail
        
        lent = len(tail)
        
        if lent != 1 : # 오름차순이라면
            temptail.sort()
            
            for i in range (lent) : 
                if temptail[i] > head[-1] : 
                    break
                
            head[-1], temptail[i] = temptail[i], head[-1]
            
            temptail.sort()
            
            for i in head + temptail :
                print (i, end = '')
            
        else : # 오름차순이 아닌 그 이외의 상황이라면
            rst = head[ : -1]
            rst.append (tail[0])
            rst.append (head[-1])
            
            
            for i in rst :
                print (i, end = '')
                
        print ()
    