# 본 문제는 그냥 30도-60도-90도 특수각을 지닌 직각삼각형 문제이다.
# 따라서 이미 주어진 30도 각도를 끼는 길이 160의 벡터는 직각삼각형에서 빗변이 된다.

import turtle

unitvector_x = 1
unitvector_y = 1

turtle.left (30)
turtle.forward (160)

k = 160 * ((80 * pow (3, 1/2)) / 160) # k는 unitvector_x의 계수. pow(3, 1/2) / 3은 cos30.
j = 160 * (1/2) # j는 unitvector_y의 계수. 1/2는 cos60.

if k == 80 * pow (3, 1/2) :
    pass

if j == 80 :
    pass

turtle.goto (0, 0)
turtle.right (30)
turtle.forward (k * unitvector_x)

turtle.left (90)
turtle.forward (j * unitvector_y)

print (k + j) 

turtle.mainloop()
