# AC
from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range (T) : 
    p = deque(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    
    dq = sys.stdin.readline().rstrip()
    
    num_d = p.count('D')
    
    if n >= 2 : # n이 2개 이상
        dq = deque(map(int, dq[1:-1].split(',')))
        
    elif n == 1 : # n 하나
        dq = deque([int(dq[1:-1])])
        
    else : # n이 0
        dq = deque()
        
    mode = 0
    cycle = 0
    
    for i in p : 
        if i == 'R' :
            mode += 1
            
        elif i == 'D' :
            if dq == deque() : # 원소가 없다면
                break
            
            else : # 원소가 있다면
                if mode % 2 == 0 : # R이 짝수개 있다면
                    dq.popleft()
                    
                else : # R이 홀수개 있다면
                    dq.pop()
                    
            num_d -= 1
                    
    if num_d == 0 and dq == deque() : 
        print ("[]")
    
    elif num_d > 0 and dq == deque() :
        print ("error")
        
    else : 
        if mode % 2 == 0 :
            print("[" + ",".join([str(k) for k in dq]) + "]")
                    
        else :
            dq.reverse()
            print ("[" + ",".join([str(k) for k in dq]) + "]")
    
    
    
    '''if i != 'D' or dq != deque() : # 마지막 명령이 D, 원소가 없는 경우 제외
        if i != 'R' or dq != deque() : 
            if n != 1 :
                if mode % 2 == 0 :
                    print("[" + ",".join([str(k) for k in dq]) + "]")
                    rst.append("[" + ",".join([str(k) for k in dq]) + "]")
                    
                else :
                    dq.reverse()
                    print ("[" + ",".join([str(k) for k in dq]) + "]")
                    rst.append ("[" + ",".join([str(k) for k in dq]) + "]")
                    
            else :
                print ("[" + str(dq[0]) + "]")
                rst.append ("[" + str(dq[0]) + "]")
            
        else : # 마지막 명령이 R, 원소가 없다면
            print ("[]")
            rst.append ("[]")
    
    else : # 마지막 명령이 D, 원소가 없다면
        if n >= 1 and dq == deque() :
            print ("[]")
            rst.append ("[]")
        
        else : 
            print ("error")
            rst.append ("error")
        
print (rst)'''