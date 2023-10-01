basket = []

N, M = map(int, input().split())

for a in range (N) :
    basket.append(0)

for b in range (M) :
    i, j, k = map(int, input().split()) # i~j, 번호 k
    
    for c in range (j - i + 1) : 
        basket[i -1 + c] = k

for d in range (len(basket)) :
    print (str(basket[d]), end = ' ')
