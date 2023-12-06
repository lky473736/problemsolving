T = int(input())

for _ in range (T) :
    n = int(input())
    
    arr = []
    suma = 0
    
    for i in range (n) : 
        compo = int(input())
        suma += compo
        arr.append ((i+1, compo))
        
    # 튜플 정렬 : https://hansuho113.tistory.com/28
    
    fo = [item[1] for item in arr]
    if fo.count(max(fo)) >= 2 : 
        print ("no winner")
    
    else : 
        arr.sort(key=lambda x: x[1], reverse=True)
        
        if (suma // 2) < arr[0][1] : 
            print (f"majority winner {arr[0][0]}")
            
        else : 
            print (f"minority winner {arr[0][0]}")
            
