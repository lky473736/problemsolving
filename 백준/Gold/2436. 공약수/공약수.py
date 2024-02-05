import sys

def euclidean(X, Y):
    if Y == 0:
        return X

    a = max(X, Y)
    b = min(X, Y)
    p = 0

    if b == 0:
        return a

    while True:
        p = a % b

        if p == 0:
            break

        a = b
        b = p

    return b
    
GCD, LCM = map(int, sys.stdin.readline().split())

times = GCD * LCM

if GCD == 1 :
    num = 2 
    min_sum = float('inf')
    pair = []
    
    while num <= times // num :
        if LCM % num == 0 and LCM % (times // num) == 0 : 
            current_sum = num + times // num
            pair = [num, times // num]
                    
            if current_sum < min_sum :
                min_sum = current_sum
                    
        num += 1 
    
else :
    num = 2
    min_sum = float('inf')
    pair = []
    
    while num <= times // num : 
        if LCM % num == 0 and LCM % (times // num) == 0 and LCM >= num :
            if euclidean(LCM//num, LCM//(times//num)) == 1 :
                if num % GCD == 0 and (times // num) % GCD == 0 and GCD <= num :
                    current_sum = num + times // num
                    pair = [num, times // num]
                        
                    if current_sum < min_sum :
                        min_sum = current_sum
        
        num += 1

if pair == [] : 
    print (GCD, LCM)
    
else :
    print (*pair)