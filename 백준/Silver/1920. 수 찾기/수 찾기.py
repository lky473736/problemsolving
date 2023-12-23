N = int(input())
resource = list(map(int, input().split()))

M = int(input())
finder = list(map(int, input().split()))

resource.sort()

for i in range (M) :
    start = 0
    end = N - 1
    
    while start < end :
        mid = (start + end) // 2
        
        if finder[i] > resource[mid] :
            start = mid + 1
            
        else :
            end = mid
            
    if finder[i] == resource[start] :
        print (1)
        
    else :
        print (0)