N, L = map(int, input().split())
hlist = list(map(int, input().split()))
hlist.sort()

now = L

for height in hlist :
    if now >= height : 
        now += 1
        
print (now)