import sys

T = int(sys.stdin.readline())

for _ in range (T) :
    N = int(sys.stdin.readline())
    list_coin = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    
    counting = [0 for _ in range (M + 1)]
    
    for coin in list_coin : 
        if coin > M : # 동전이 구하고자 하는 값보다 크면
            continue 
        
        counting[coin] += 1
        
        for i in range (coin + 1, M + 1) : 
            counting[i] += counting[i-coin]
    
    print (counting[M])