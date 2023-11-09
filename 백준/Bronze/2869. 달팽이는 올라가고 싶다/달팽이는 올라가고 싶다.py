import sys

A, B, V = map(int, sys.stdin.readline().split())

'''
step, day = 0, 1

while True : 
    step = step + A
    
    if step >= V :
        break
    
    step = step - B
    
    if step >= V :
        break
    
    day = day + 1''' # <- 시간 초과

day = (V - B - 1) // (A - B) + 1
print (day)
