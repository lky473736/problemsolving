cycle = 1

N = input()

if int(N) < 10 :
    N = '0' + N
    
nextnum = N[-1] + str(int(N[0]) + int(N[-1]))[-1]

    
while True :
    if nextnum == N : 
        break
    
    nextnum = nextnum[-1] + str(int(nextnum[0]) + int(nextnum[-1]))[-1]
    cycle += 1
    
print (cycle)