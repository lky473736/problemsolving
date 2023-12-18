N = int(input())
order = list(map(int, input().split()))
rst = [0 for i in range (N)]

for i in range (N):
    cnt = 0 

    for j in range (N) :
        if cnt == order[i] and rst[j] == 0 :
            rst[j] = i + 1
            break

        elif rst[j] == 0:
            cnt += 1

for i in rst :
    print (i, end = ' ')