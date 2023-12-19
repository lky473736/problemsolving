x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if 1 :
    # https://coloredrabbit.tistory.com/162
    # https://www.acmicpc.net/blog/view/27
    
    comp = (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)
    
    if comp > 0 :
        print (-1)
        
    elif comp < 0 :
        print (1)
        
    else :
        print (0)
