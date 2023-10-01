basket = []

N, M = map(int, input().split())

for a in range (N) :
    basket.append(a + 1)
    
for b in range (M) :
    i, j = map(int, input().split())
    
    # https://growingarchive.tistory.com/146
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for c in range (len(basket)) :
    print (basket[c], end = ' ')
