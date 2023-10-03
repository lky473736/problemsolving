'''A, B, C = map(int, input().split())
D = int(input())

sec = C + D
minute = B
hour = A

if sec >= 60 :
    sec = sec % 60
    minute += sec // 60
    
    if minute >= 60 :
        minute += minute % 60
        hour += minute // 60
        
        if hour > 23 :
            hour == hour % 24
            
print (hour, minute, sec)'''

A, B, C = map(int, input().split())
D = int(input())

sec = C + D
minute = B
hour = A

if sec >= 60:
    minute += sec // 60
    sec = sec % 60

if minute >= 60:
    hour += minute // 60
    minute = minute % 60

if hour >= 24:
    hour = hour % 24

print(hour, minute, sec)