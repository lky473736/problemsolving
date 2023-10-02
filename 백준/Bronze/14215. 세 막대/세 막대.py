num = list(map(int, input().split()))

if sorted(num)[-1] < sorted(num)[0] + sorted(num)[1] :
    print (sum(num))
    exit()
    
else : 
    print (sorted(num)[0] + sorted(num)[1] + sorted(num)[0] + sorted(num)[1] - 1)