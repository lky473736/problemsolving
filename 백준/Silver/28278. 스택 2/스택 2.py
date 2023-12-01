import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    compo = sys.stdin.readline().split()  # .rsplit() 대신 .split()을 사용하여 공백을 기준으로 나누도록 수정
    
    if len(compo) >= 2:  # compo의 길이가 2 이상이면 수행
        tra, X = compo  # compo를 분할하여 tra와 X로 나눔
        if tra == '1':  # '1'이면 X를 스택에 추가
            stack.append(int(X))
    
    if compo == ['2']:  # compo가 리스트이므로 ['2']와 비교하여 수정
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
            
    elif compo == ['3']:  # 비교하는 값도 리스트로 수정
        print(len(stack))
        
    elif compo == ['4']:  # 비교하는 값도 리스트로 수정
        if not stack:
            print(1)
        else:
            print(0)
    
    elif compo == ['5']:  # 비교하는 값도 리스트로 수정
        if stack:
            print(stack[-1])
        else:
            print(-1)