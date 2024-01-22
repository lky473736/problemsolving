import sys

H, W = map(int, sys.stdin.readline().split())
list_block = list(map(int, sys.stdin.readline().split()))

counting_all = 0

for i in range (H) :
    list_lego = [0 for i in range (W)]
    
    for j in range (W) : 
        if list_block[j] > 0 :
            list_lego[j] += 1
            list_block[j] -= 1
    
    chmod = 0
    
    counting_current = 0
    
    for j in range (W) :
        if j == 0 or j == W - 1:
            if list_lego[j] == 0 :
                counting_current = 0
                continue
        
        if list_lego[j] == 1 :
            if chmod == 1 and list_lego[j-1] == 0 :
                chmod = 0
                counting_all += counting_current
                counting_current = 0
        
        elif list_lego[j] == 0 :
            if list_lego[j-1] == 1:
                chmod = 1
                counting_current += 1
                
            else :
                if chmod == 1 :
                    counting_current += 1
        
print (counting_all)