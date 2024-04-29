import sys

n = int(sys.stdin.readline())

student = dict()
fee = list()

for i in range (n) :
    time, name = sys.stdin.readline().rstrip().split()
    hour, minute = int(time[0:2]), int(time[3:])
    
    try : 
        student[name] += hour * 60 + minute
        
    except :
        student[name] = hour * 60 + minute
        
for name in student.keys() :
    value = 10
    
    # print (name, student[name])
    
    if student[name] <= 100 : 
        pass
    
    else :
        student[name] -= 100
        
        if student[name] % 50 != 0 :
            value += ((student[name] // 50) + 1) * 3
            
        else :
            value += (student[name] // 50) * 3
    
    fee.append ([name, value])
    
fee.sort (key = lambda x : (-x[1], x[0]))

for compo in fee :
    print (compo[0], compo[1])