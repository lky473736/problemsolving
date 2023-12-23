N = int(input())

garo = 0
sero = 0

arr = []

for _ in range (N) :
    row = input()
    trow = list(row.split('X'))
    
    counting = 0
    
    for i in trow :
        if len(i) >= 2 :
            counting += 1
        
    garo += counting
    
    arr.append(row)

arr = [[arr[i][j] for i in range(N)] for j in range(N)]
arr = [''.join(arr[i]) for i in range(N)]

for column in arr :
    tcolumn = list(column.split('X'))
    
    counting = 0
    
    for i in tcolumn :
        if len(i) >= 2 :
            counting += 1
        
    sero += counting
        
print (garo, sero)