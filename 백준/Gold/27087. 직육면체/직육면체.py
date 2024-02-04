T = int(input())

for _ in range (T) :
    A, B, C, p = map(int, input().split())
    
    if (B % p == 0 and C % p == 0) or (A % p == 0 and B % p == 0) or (A % p == 0 and C % p == 0) :
        print (1)
        
    else :
        print (0)