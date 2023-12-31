import sys

n = int(sys.stdin.readline())

breakkey = 0
rst = []

for i in range(0, 224) :
    for j in range(0, 224) :
        for k in range (0, 224) :
            for p in range(0, 224) :
                if i ** 2 + j ** 2 + k ** 2 + p ** 2 == n :
                    rst = [i, j, k, p]
                    breakkey = 1
                    break
                
            if breakkey == 1 :
                break
            
        if breakkey == 1 :
            break
        
    if breakkey == 1 :
        break

rst = [i for i in rst if i != 0]
print(len(rst))
