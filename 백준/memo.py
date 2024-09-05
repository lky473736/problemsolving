import math
import sys

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())

# equation's coefficient and constant
# only one
component = {'a' : -2*x1 + 2*x2, 'b' : -2*y1 + 2*y2, 'c' : (x1**2 - x2**2) + (y1**2 - y2**2) - r1**2 + r2**2}

# distance between two meeting point
d1 = abs(component['a']*x1 + component['b']*y1 + component['c']) / (component['a']**2 + component['b']**2)

# distance between two center
d2 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

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
