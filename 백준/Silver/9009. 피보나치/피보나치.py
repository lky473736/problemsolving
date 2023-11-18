def fibornacci (N) : # more of 2
    a0 = 0
    a1 = 1
    
    compo = 0 
    
    for i in range (N - 1) : 
        compo = a0 + a1
        a0 = a1
        a1 = compo
    
    return compo

f_list = [0, 1]
i = 2

while f_list[-1] < 1000000000 :
    f_list.append(fibornacci(i))
    i += 1
    
f_list.sort(reverse = True)
    
T = int(input())

for i in range (T) :
    finder = []
    num = int(input())
    
    while num != 0 :
        for j in f_list : 
            if j <= num : 
                finder.append(j)
                minus = j
                break
            
        num -= minus
        
    for compo in finder[::-1] :
        print (compo, end = ' ')
    print ()