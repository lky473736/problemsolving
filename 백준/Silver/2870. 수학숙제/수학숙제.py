import sys
import re

N = int(sys.stdin.readline())

slist = []

'''for i in range (N) :
    compo = sys.stdin.readline()
    numbers = ''.join(filter(str.isdigit, compo))
    slist.append (numbers)'''
    
for i in range(N) :
    compo = sys.stdin.readline()  # 사용자로부터 문자열 입력 (예: j132p1)
    numbers = re.findall(r'\d+', compo)  # 숫자만 찾기
    numbers = list(map(int, numbers))  # 문자열 숫자를 정수형으로 변환
    
    for j in numbers :
        slist.append (j)
            
slist.sort()

for j in slist :
    print (j)