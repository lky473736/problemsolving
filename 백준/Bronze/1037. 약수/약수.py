N = int(input())
yaksu = list(map(int, input().split()))

yaksu.sort()

if len(yaksu) == 1 :
    print (yaksu[0] ** 2)
    
else : 
    print (yaksu[0] * yaksu[-1])