# import sys

# x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
# x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

# if x1 > x2 : 
#     L1 = [[x2, y2], [x1, y1]]
    
# else : 
#     L1 = [[x1, y1], [x2, y2]]

# if x3 > x4 :
#     L2 = [[x4, y4], [x3, y3]]
    
# else : 
#     L2 = [[x3, y3], [x4, y4]]
    
# # print (L1, L2)

# # 기울기
# token_0_divide = [0, 0]

# try : 
#     m1 = (L1[0][1] - L1[1][1]) / (L1[0][0] - L1[1][0])
# except ZeroDivisionError : 
#     token_0_divide[0] = 1

# try : 
#     m2 = (L2[0][1] - L2[1][1]) / (L2[0][0] - L2[1][0])
# except ZeroDivisionError : 
#     token_0_divide[1] = 1

# # 둘 다 x = ~~
# if token_0_divide == [1, 1] :
#     # 둘 다 동일한 x라면
#     if L1[0][0] == L2[0][0] : 
#         print (1)
        
#     else : 
#         print (0)
        
#     exit()
        
# else : # 하나만 x = ~~~
#     if token_0_divide[0] == 1 or token_0_divide[1] == 1 :
#         if token_0_divide[0] == 1 : 
#             mx = L1[0][0]
#             my = m2*mx - m2*L2[1][1] + L2[1][1]
            
#             if L2[0][0] <= mx <= L2[1][0] :
#                 if L1[0][1] <= my <= L1[1][1]
            
#         else : 
#             mx = L2[0][0]
#             my = m1*mx - m1*L1[1][1] + L1[1][1]
        
        
# # 기울기가 동일하다면
# if m1 == m2 : 
#     # 둘 다 y = ~~~
#     if m1 == 0 :
#         # 둘 다 동일한 y값이라면
#         if L1[0][1] == L2[0][1] :
#           print (1)
        
#         else : 
#           print (0)

#     else :
#         print (0)
        
# else : # 기울기가 다르다면
#     # 교점 : mx, my
#     mx = ((m2*L2[1][0] - m1*L1[1][0]) - (L2[1][1] - L1[1][1])) / (m2 - m1)
#     my = m2*mx - m2*L2[1][0] + L2[1][1]
    
#     # L1의 x를 1씩 증가시켜서 확인
#     for dx in range (L1[0][0], L1[1][0]) : 
#         # print (dx, mx, dx+1)
#         if dx <= mx <= dx+1 :
#             # print (m1*(dx-L1[1][0])+L1[1][1], my, m1*(dx+1-L1[1][0])+L1[1][1])
#             if m1*(dx-L1[1][0])+L1[1][1] <= my <= m1*(dx+1-L1[1][0])+L1[1][1] :
#                 print (1) 
#                 exit()
            
#     print (0)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if x1 > x2:
    L1 = [[x2, y2], [x1, y1]]
else:
    L1 = [[x1, y1], [x2, y2]]

if x3 > x4:
    L2 = [[x4, y4], [x3, y3]]
else:
    L2 = [[x3, y3], [x4, y4]]

token_0_divide = [0, 0]

try:
    m1 = (L1[0][1] - L1[1][1]) / (L1[0][0] - L1[1][0])
except ZeroDivisionError:
    token_0_divide[0] = 1
    m1 = None  

try:
    m2 = (L2[0][1] - L2[1][1]) / (L2[0][0] - L2[1][0])
except ZeroDivisionError:
    token_0_divide[1] = 1
    m2 = None  

# If both lines are vertical
if token_0_divide == [1, 1]:
    if L1[0][0] == L2[0][0]:
        print(1)
    else:
        print(0)
    exit()

if token_0_divide[0] == 1 or token_0_divide[1] == 1:
    if token_0_divide[0] == 1:  # L1 is vertical
        mx = L1[0][0]
        my = m2 * (mx - L2[1][0]) + L2[1][1]
    else:  # L2 is vertical
        mx = L2[0][0]
        my = m1 * (mx - L1[1][0]) + L1[1][1]

    if L1[0][0] <= mx <= L1[1][0] and L2[0][0] <= mx <= L2[1][0] and \
            min(L1[0][1], L1[1][1]) <= my <= max(L1[0][1], L1[1][1]) and \
            min(L2[0][1], L2[1][1]) <= my <= max(L2[0][1], L2[1][1]):
        print(1)
    else:
        print(0)
    exit()

if m1 == m2:  
    if m1 == 0:
        if L1[0][1] == L2[0][1]:
            print(1)
        else:
            print(0)
        exit()
    else:
        print(0) 
        exit()

b1 = L1[0][1] - m1 * L1[0][0]
b2 = L2[0][1] - m2 * L2[0][0]

mx = (b2 - b1) / (m1 - m2)
my = m1 * mx + b1

if (L1[0][0] <= mx <= L1[1][0] and min(L1[0][1], L1[1][1]) <= my <= max(L1[0][1], L1[1][1])) and \
   (L2[0][0] <= mx <= L2[1][0] and min(L2[0][1], L2[1][1]) <= my <= max(L2[0][1], L2[1][1])):
    print(1)
else:
    print(0)
