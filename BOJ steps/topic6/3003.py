chess = [1, 1, 2, 2, 2, 8]

havelist = list(map(int, input().split()))
needlist = []

for i in range (len(chess)):
    if chess[i] == havelist[i] :
        needlist.append(0)
    
    elif chess[i] != havelist[i] : 
        num = chess[i] - havelist[i]
        needlist.append (num)
        
for j in needlist :
    print (j, end = ' ')
