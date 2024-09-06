'''
import math
import sys

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())

# equation's coefficient and constant
# only one
component = {'a' : -2*x1 + 2*x2, 'b' : -2*y1 + 2*y2, 'c' : (x1**2 - x2**2) + (y1**2 - y2**2) - (r1**2 - r2**2)}

# distance between two center
d2 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# distance between two meeting point
d1 = math.sqrt(r1**2 - (0.5*d2)**2) * 2

# left angle and right angle
angle_left = math.acos((r1**2 + d2**2 - r2**2) / (2 * r1 * d2))
angle_right = math.acos((r2**2 + d2**2 - r1**2) / (2 * r2 * d2))

# new angle
new_angle_left = math.pi/2 - angle_left
new_angle_right = math.pi/2 - angle_right

# calculating the triangle
tri_left = 0.5**2 * r1 * d1 * math.sin(new_angle_left)
tri_right =  0.5**2 * r2 * d1 * math.sin(new_angle_right)

# calculating the cal sector (radian way)
sector_left = 0.5 * r1**2 * angle_left
sector_right = 0.5 * r2**2 * angle_right

# rst
rst = (sector_left - tri_left) * 2 + (sector_right - tri_right) * 2

print (rst)
'''

import math
import sys

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())

# equation's coefficient and constant
# only one
# component = {'a' : -2*x1 + 2*x2, 'b' : -2*y1 + 2*y2, 'c' : (x1**2 - x2**2) + (y1**2 - y2**2) - (r1**2 - r2**2)}

# distance between two center
d2 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

rst = 0

if d2 == 0 : # if equal
    if x1 == x2 and y1 == y2 :
        rst = math.pi * min(r1, r2)**2

else : 
# check if circles don't intersect or one contains the other
    if d2 >= r1 + r2  : # meet one point or not meet outside
        rst = 0
        
    if d2 <= abs(r1 - r2) : # meet one point or not meet inside
        rst = math.pi * min(r1, r2)**2
 
    if d2 > abs(r1 - r2) and d2 < r1 + r2 : 
        # meet at the area 
        # left angle and right angle
        angle_left = math.acos((r1**2 + d2**2 - r2**2) / (2 * r1 * d2))
        angle_right = math.acos((r2**2 + d2**2 - r1**2) / (2 * r2 * d2))

# # new angle
# new_angle_left = math.pi/2 - angle_left
# new_angle_right = math.pi/2 - angle_right

# # calculating the triangle
# tri_left = 0.5**2 * r1 * d1 * math.sin(new_angle_left)
# tri_right =  0.5**2 * r2 * d1 * math.sin(new_angle_right)

# # calculating the cal sector (radian way)
# sector_left = 0.5 * r1**2 * angle_left
# sector_right = 0.5 * r2**2 * angle_right

        # distance between two meeting point (half)
        d1 = r1 * math.sin(angle_left) 

        # rst
        compo1 = 0.5 * (r1**2) * angle_left - 0.5 * d1 * r1 * math.cos(angle_left)
        compo2 = 0.5 * (r2**2) * angle_right - 0.5 * d1 * r2 * math.cos(angle_right)

# rst = (sector_left - tri_left) * 2 + (sector_right - tri_right) * 2
        rst = compo1 * 2 + compo2 * 2

if rst != 0 : 
    print (round(1000*rst) / 1000)

else :
    print ('0.000')