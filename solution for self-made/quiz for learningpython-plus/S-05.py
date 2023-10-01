# 참고 : https://chojaeyou064.tistory.com/1

import random

def montyhall(time) :
    carget, goat = 0, 0
    
    for i in range(time) :
        car = random.randint(0, 2) 
        doors = [0, 0, 0] 

        doors[car] = 1

        firstchoice = random.randint(0, 2)

        if doors[firstchoice] == 0 : 
            doors[firstchoice] += -1
        else :
            doors[firstchoice] = -2

        doors.remove(0) 

        if -1 in doors :
            carget += 1
            
        else :
            goat += 1 

    arr = [carget, goat, carget + goat]
    if carget + goat != 0 :
        arr.append(carget / (carget + goat))
    else :
        arr.append(0)
    return arr

num = int(input("몬티홀을 반복할 횟수를 입력하세요 : "))

for k in range(num) :
    print (montyhall(k))

finalarr = montyhall(num)

print ("따라서 확률은 : ", finalarr[3])