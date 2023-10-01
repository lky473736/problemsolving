slist = []

for i in range (9) :
    k = int(input())
    slist.append (k)

print (max(slist)) # max 매소드 사용
print (slist.index(max(slist)) + 1)
