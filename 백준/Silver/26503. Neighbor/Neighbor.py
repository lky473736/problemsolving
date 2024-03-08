'''
두 분수가 "이웃"이라고 생각되는 경우는 두 분수 사이의 최소 양의 차이의 분자가 1인 경우입니다. 예를 들어, 분수 1/11과 1/12는 1/132가 되므로 "이웃"입니다. 그러나 2/5와 4/5는 차이가 2/5이므로 "이웃"이 아닙니다. "이웃" 분수 값을 결정하고 출력하거나 "이웃이 아님"을 출력합니다.


입력의 첫 번째 줄에는 데이터 세트의 수를 나타내는 단일 양의 정수 n이 포함되어 있습니다. 각 데이터 세트는 분자, 분모, 분자, 분모의 순서로 구성된 두 양의 정수 값으로 구성되며, 모두 하나의 줄에 공백으로 구분되어 있습니다.
'''

import sys

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

n = int(sys.stdin.readline())

for _ in range (n) :
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    
    if x1 == x2 : 
        if abs(y1 - y2) == 1 :
            print (f"1/{x1}")
            
        else :
            print ("NOT NEIGHBORS")
            
    else :
        LCM = (x1 * x2) // euclidean (x1, x2)
        diff = abs(y1*(LCM//x1) - y2*(LCM//x2))
        
        i = 2
        
        while i < LCM or i < diff :
            if LCM % i == 0 and diff % i == 0 :
                LCM = LCM // i
                diff = diff // i
                
            else :
                i += 1
                
        if diff == 1 :
            print (f"{diff}/{LCM}")
            
        else :
            print ("NOT NEIGHBORS")