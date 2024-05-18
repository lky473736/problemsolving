'''


문제
미국 사회보장국(SSA)에서 큰 실수를 저질렀습니다. 새로운 사회보장번호(SSN)를 미국 시민에게 할당하는 과정에서 중복된 번호를 할당한 것입니다. 
다행히도 이 문제를 조기에 발견하여, 가능한 모든 중복 번호의 목록을 가지고 있습니다. 사회보장국은 중복된 SSN을 가지고 있는 모든 사람에게 연락해야 합니다. 여러분의 임무는 사회보장번호 목록을 읽어 중복된 번호를 찾아내는 것입니다. 그런 다음 중복된 번호 목록을 오름차순으로 출력하세요.

입력
입력은 한 줄에 하나의 사회보장번호로 이루어져 있습니다. 입력은 중복되지 않은 사회보장번호 000-00-0000으로 종료됩니다.

'''

import sys

tel = []
book = dict()

while True :
    try : 
        # sentence = map(int, sys.stdin.readline().rstrip().split('-'))
        
        sentence = sys.stdin.readline().rstrip()
        # print (sentence)
        
        if sentence == "000-00-0000" : 
            break
        
        # tel.append ([a, b, c])
        
        try : 
            book[sentence] += 1
            
            if book[sentence] == 2 : 
                a, b, c = map(int, sentence.split('-'))
                tel.append ([sentence, [a, b, c]]) 
            
        except : 
            book[sentence] = 1 
            
    except : 
        break
    
tel = sorted (tel, key = lambda x : (x[1][0], x[1][1], x[1][2]))

for compo in tel : 
    print (compo[0])