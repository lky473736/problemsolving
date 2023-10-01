# https://jokerkwu.tistory.com/154

startpoint = 3 ** 2

N = int(input())

if N - 1 == 0 :
    print (startpoint)
    
else : 
    for i in range(N - 1):
        lastpoint = ((startpoint ** 0.5) + (2 ** (i + 1))) ** 2

        startpoint = lastpoint
        
    print (int(lastpoint))
