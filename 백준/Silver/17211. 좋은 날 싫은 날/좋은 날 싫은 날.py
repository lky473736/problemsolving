import sys

N, F = map(int, sys.stdin.readline().split())
p1, p2, p3, p4 = map(float, sys.stdin.readline().split())

b = 0.0
g = 0.0

if F == 0 :
    g = 1.0
    
else :
    b = 1.0

for i in range (N) :
    preg = g
    g = g * p1 + b * p3
    b = preg * p2 + b * p4
    
print (int(g*1000))
print (int(b*1000))