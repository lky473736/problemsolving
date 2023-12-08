H, W = map(int, input().split())

rst = [[-1 for i in range (W)] for j in range (H)]

for i in range (H) :
    compo = list(input())
    
    for j in range (W) : 
        if compo[j] == 'c' :
            temp = j
            startpoint = 0
            while temp != W : 
                rst[i][temp] = startpoint
                temp += 1
                startpoint += 1
                
            rst[i][j] = 0
            
for i in rst : 
    for compo in i : 
        print (compo, end = ' ')
        
    print ()