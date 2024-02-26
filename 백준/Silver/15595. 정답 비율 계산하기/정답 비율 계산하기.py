import sys

N = int(sys.stdin.readline())

get_wrong = 0
get_right = 0
winuser = set()
userdict = dict()

for _ in range (N) :
    num, userId, rst, mem, time, lang, leng = sys.stdin.readline().rstrip().split()
    num = int(num)
    rst = int(rst)
    mem = int(mem)
    time = int(time)
    lang = int(lang)
    leng = int(leng)
    
    if N == 1 and userId == 'megalusion' :
        print ('0.00')
        exit() # 예외
        
    if userId == 'megalusion' : 
        continue
    
    if userId not in userdict.keys() :
        userdict[userId] = 0
        
    if rst == 4 and (userId not in winuser) == True :
        get_wrong += userdict[userId]
        get_right += 1
        winuser.add(userId)
        
    elif rst != 4 and (userId not in winuser) == True :
        userdict[userId] += 1
            
    elif rst != 4 and (userId in winuser) == True :
        pass
    
    elif rst == 4 and (userId in winuser) == True :
        pass

try : 
    rate = "{:.10f}".format((get_right / (get_right + get_wrong)) * 100)
    print (rate)
    
except ZeroDivisionError :
    print (0)