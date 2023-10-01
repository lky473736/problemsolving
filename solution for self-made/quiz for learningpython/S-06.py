# 밑변과 높이를 이용하여 이등변삼각형을 그리는 turtle 프로그램
# radian angle -> 60 way to angle (at natural position)
# 극좌표계 계산과 valueerror 방지를 위해 atan2 사용 (그렇게 흔한 버그는 아니니 acos로 사용)

import turtle
import math

wid = int(turtle.textinput("", "밑변 입력 : "))
hei = int(turtle.textinput("", "높이 입력 : "))

ang = math.degrees(math.acos((1/2 * (wid)) / pow (pow(hei, 2) + 1/4 * pow(wid, 2), 1/2)))
# ang = math.degrees(math.atan2(hei, wid/2))
betang = 180 - 2 * ang

turtle.goto(0,0)
turtle.fd(wid)
turtle.lt(180 - ang)
turtle.fd(math.sqrt(hei**2 + (wid/2)**2))
turtle.lt(180 - betang)
turtle.fd(math.sqrt(hei**2 + (wid/2)**2))

turtle.mainloop()
