N = int(input())
slist = list(input().split())
tier = ['B', 'S', 'G', 'P', 'D']

for i in range(N) : 
    slist[i] = (slist[i][0], int(slist[i][1:]))

temp = slist.copy()
slist = sorted(slist, key=lambda x: (x[0], -x[1]))

if 1 == 1 :  
    rst = []
    
    while True :
        num = [i[0] for i in slist].count('B')
        ab = 'B'

        if [i[0] for i in slist].count('B') == 0 :
            num = [i[0] for i in slist].count('S')
            ab = 'S'
            if [i[0] for i in slist].count('S') == 0 :
                num = [i[0] for i in slist].count('G')
                ab = 'G'
                if [i[0] for i in slist].count('G') == 0 :
                    num = [i[0] for i in slist].count('P')
                    ab = 'P'
                    if [i[0] for i in slist].count('P') == 0 :
                        num = [i[0] for i in slist].count('D')
                        ab = 'D'
                        if [i[0] for i in slist].count('D') == 0 :
                            break

        rst.append (slist[[i[0] for i in slist].index(ab)])
        slist.pop([i[0] for i in slist].index(ab))
    
    if rst == temp : 
        print ('OK')
        
    else :
        print ('KO')
        finder = []
        
        for i in range (N) :
            if temp[i] != rst[i] :
                finder.append (rst[i])
        
        for i in finder : 
            print (f'{i[0]}{i[1]}', end = ' ')