n, d = map(int, input().split())
count = 0

for i in range (1, n + 1) : 
    if str(d) in str(i) : 
        count += str(i).count(str(d))

print (count)