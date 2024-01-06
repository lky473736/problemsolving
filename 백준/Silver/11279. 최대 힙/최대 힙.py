import heapq
import sys

N = int(sys.stdin.readline())

heap_abs = []

'''for _ in range (N) :
    compo = int(sys.stdin.readline())
    
    if compo != 0 :
        heapq.heappush(heap_abs, compo)
        
    else :
        if heap_abs == [] : 
            print (0)
        
        else :
            update = []
            # https://ojt90902.tistory.com/820
            for num in heap_abs :
                heapq.heappush(update, (abs(num), num))
                
            heap_abs = [i[1] for i in update]
              
            print (heap_abs[0])
            heap_abs.pop(0)'''

for idx in range (N) :
    num = int(sys.stdin.readline())
    
    if num != 0 :
        heapq.heappush (heap_abs, (-num, num))
        
    else :
        try :
            print (heapq.heappop(heap_abs)[1])
            
        except IndexError :
            print (0)