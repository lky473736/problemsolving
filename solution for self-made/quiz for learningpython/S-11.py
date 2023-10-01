# turtle와 random을 이용한 행위예술 ver.2

import turtle as t
import random 

t.colormode(255) # 3-tuple로 rgb 값 받기
t.speed (0)

def moverandomly(b) : # 움직임 함수
    t.goto(random.randint(-200, 200), random.randint(-200, 200))

def crazytriangle(a) : # 삼각형 그리기 (재귀변수 a)
    for j in range (a) : 
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        
        dir = random.randint(1, 2)
        len = random.randint(1, 200)
        
        t.write("%s, %s, %s" %(r, g, b)) # 삼각형 각각의 rgb 값 모니터에 출력
        
        t.pencolor(r, g, b)
        
        for i in range (3) :
            t.fd(len)
            if dir == 1 :
                t.rt(120)
            else :
                t.lt(120)
            
        t.penup()
        moverandomly(a)
        t.pendown()
        

val = int(t.textinput("", "삼각형 갯수 : "))

crazytriangle(val)

t.mainloop()
