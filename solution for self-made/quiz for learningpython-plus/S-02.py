import random
from tkinter import *
from PIL import Image, ImageTk

window = Tk()

# selection algorithm
'''if op1 == 1 :
    if op2 == 1 :
        if op3 == 1 :
            
        elif op3 == 2 :
            
        elif op3 == 3 :
            
        elif op3 == 4 : 
            
    elif op2 == 2 :
        if op3 == 1 :
            
        elif op3 == 2 :
            
        elif op3 == 3 :
            
        elif op3 == 4 : 
    
    elif op2 == 3 :
        if op3 == 1 :
            
        elif op3 == 2 :
            
        elif op3 == 3 :
            
        elif op3 == 4 : 
        
    elif op2 == 4 : 
        if op3 == 1 :
            
        elif op3 == 2 :
            
        elif op3 == 3 :
            
        elif op3 == 4 : ''' # 더 이상은 노역이자 노가다
    
    
a = random.randint (0, 100)
b = random.randint (0, 100)
c = random.randint (0, 100)
d = random.randint (0, 100)

# 소수점이 생기지 않게끔 (정수형이 나오게끔) / 기호 없앰
operators = ['+', '-', '*']
variables = [a, b, c, d]

expressions = []

# 4개의 변수에 대한 모든 조합 생성
for i, a in enumerate(variables):
    for j, b in enumerate(variables):
        if j == i:
            continue
        for k, c in enumerate(variables):
            if k == i or k == j:
                continue
            for l, d in enumerate(variables):
                if l == i or l == j or l == k:
                    continue
                # 사칙연산 연산자를 포함한 식 생성
                for op1 in operators:
                    for op2 in operators:
                        for op3 in operators:
                            expression = f"{a} {op1} {b} {op2} {c} {op3} {d}"
                            expressions.append(expression)

# 결과 출력
for expression in expressions:
    print(expression)
    
def confirm():
    global l  # 전역 변수 선언
    inp = float(e1.get())
    if inp == ans:
        img = ImageTk.PhotoImage(Image.open("/Users/alphastation/Desktop/repository/problemsolving/solution for self-made/quiz for learningpython-plus/good.jpeg"))
        l.configure(image=img)  # 이미지 업데이트
        l.image = img  # 이미지 객체에 대한 참조 유지
    elif inp != ans:
        img = ImageTk.PhotoImage(Image.open("/Users/alphastation/Desktop/repository/problemsolving/solution for self-made/quiz for learningpython-plus/sad.jpeg"))
        l.configure(image=img)  # 이미지 업데이트
        l.image = img  # 이미지 객체에 대한 참조 유지

        realans = Label(window, text="정답은 " + str(ans))
        realans.pack()

formula = random.choice(expressions)
ans = eval(formula) # 식을 계산하는 함수 eval
print (ans)

l1 = Label(window, text="컴퓨터가 내는 문제를 맞춰보세요!")
l2 = Label(window, text=formula, fg="blue")

l1.pack()
l2.pack()

e1 = Entry(window)
btn = Button(window, text="결과 제출", command=confirm)

e1.pack()
btn.pack()

l = Label(window)  # 이미지를 표시할 라벨 생성
l.pack()

window.mainloop()