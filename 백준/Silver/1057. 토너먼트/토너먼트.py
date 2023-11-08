N, K, L = map(int, input().split())

slist = [i for i in range (1, N + 1)]

slist[K - 1] = -1
slist[L - 1] = -2

def calculate_rounds(n):
    log_value = 0
    while n > 1:
        n /= 2
        log_value += 1
    return log_value

allround = calculate_rounds(N)

for repeatenum in range (allround) :
    finder = []
    if len(slist) % 2 == 0 : # 짝수면
        for p in range (0, len(slist), 2) : 
            if (slist[p] == -1 and slist[p + 1] == -2) or (slist[p] == -2 and slist[p + 1] == -1) : 
                print (repeatenum + 1)
                exit()
            
            else :
                if -1 in slist[p:p+2] :
                    finder.append (-1)
                elif -2 in slist[p:p+2] :
                    finder.append (-2)
                else :
                    finder.append (slist[p])
                    
        slist = finder
        
    else : # 홀수면
        for p in range (0, len(slist) - 1, 2) : 
            if (slist[p] == -1 and slist[p + 1] == -2) or (slist[p] == -2 and slist[p + 1] == -1) : 
                print (repeatenum + 1)
                exit()
            
            else :
                if -1 in slist[p:p+2] :
                    finder.append (-1)
                elif -2 in slist[p:p+2] :
                    finder.append (-2)
                else :
                    finder.append (slist[p])
        
        if slist[-1] == -1 :
            finder.append(-1)
        
        elif slist[-1] == -2 :
            finder.append(-2)
            
        else :
            finder.append(slist[-1])
            
        slist = finder
        
    
print (-1)